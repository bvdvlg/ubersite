from fastapi import FastAPI
import docker
import pathlib
from time import sleep
import json
from starlette.responses import Response
BASE_DIR = pathlib.Path(__file__).parent.resolve()

app = FastAPI()
client = docker.from_env()
REQUEST_TIMEOUT = 10000
SLEEP_TIMEOUT = 200

with open("configuration/task_description.json", "r") as file:
    configuration = json.load(file)
print(configuration)

@app.get("/execute")
async def execute(task: str):
    print(BASE_DIR)
    mount = docker.types.Mount(target='/code/task_code', source='{}/{}'.format(BASE_DIR, 'task_executor/task_code'), type='bind', read_only=True)
    if configuration.get(task) is None:
        return Response("This task isn't exists")

    container = client.containers.run(
        image=configuration[task]["image"], 
        detach=True, 
        mounts=[mount,], 
        auto_remove=False, 
        stdout=True, 
        environment=["TASK_NAME={}".format(task), "TASK_DIR={}".format('/code/task_code')]
    )
    container.reload()

    container.wait(timeout=REQUEST_TIMEOUT)

    print(container.logs())

    try:
        container.kill()
    except docker.errors.NotFound:
        pass
    except docker.errors.APIError:
        pass
    container.remove()
