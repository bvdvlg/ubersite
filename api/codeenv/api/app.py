from fastapi import FastAPI
import docker
import pathlib
import json
from starlette.responses import Response
from configuration.settings import codeenv_executor_settings
import requests
from api.library.docker_manager import DockerContainerExecutorWrapper
from api.library.file_manager import UserFolderManager
from api.model import PythonCode
from time import sleep
BASE_DIR = pathlib.Path(__file__).parent.resolve()

app = FastAPI()
client = docker.from_env()
REQUEST_TIMEOUT = 10

@app.post("/execute")
async def execute(code: PythonCode):
    error_response = Response(status_code=0)

    with UserFolderManager(codeenv_executor_settings.user_code_dir) as fm:
        with fm.create_file('main.py') as file:
            file.write(code.code)
            user_code_hash = fm.user_code_hash

        with DockerContainerExecutorWrapper(client, error_response, detach=True, auto_remove=False, stdout=True) as container:
            container.add_mount(docker.types.Mount(target="{}/{}".format(codeenv_executor_settings.user_code_mountpoint, user_code_hash), source="{}/{}".format(codeenv_executor_settings.user_code_dir, user_code_hash), type='bind', read_only=True))
            if code.library is not None:
                container.add_mount(docker.types.Mount(target="{}/{}".format(codeenv_executor_settings.lib_code_mountpoint, code.library), source="{}/{}".format(codeenv_executor_settings.lib_code_dir, code.library), type='bind', read_only=True))

            container.set_image("{}/codeenv/{}".format(codeenv_executor_settings.repository, code.image))

            container.add_environment_var("TASK_ID", user_code_hash)
            container.add_environment_var("PYTHONPATH", "{}/{}".format(codeenv_executor_settings.user_code_mountpoint, user_code_hash))
            if code.library is not None:
                container.append_environment_var("PYTHONPATH", "{}/{}".format(codeenv_executor_settings.lib_code_mountpoint, code.library))

            container.run()
            exit_code = container.wait(timeout=REQUEST_TIMEOUT)

            stderr_log = container.check_stderr()
            stdout_log = container.check_stdout()
    if error_response.status_code:
        return error_response
    return Response(content=json.dumps({"stderr": stderr_log, "stdout": stdout_log, "exit_code": exit_code}), status_code=200)
