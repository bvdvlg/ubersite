from io import BytesIO
import uvicorn
import argparse
import os

import docker
import os
from time import sleep
import requests, json

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="Defines the environment of project")
parser.add_argument("-p", "--port", type=int, help="Defines the environment of project")
parser.add_argument("-e", "--env", type=str, help="Defines the environment of project")

USER_CODE_DIR_NAME_DEFAULT = "user_code"

if __name__ == "__main__":
    sleep(1000)
    user_code_dir = os.environ.get("code_executor_user_code_dir") or USER_CODE_DIR_NAME_DEFAULT
    registry_host = os.environ.get("code_executor_registry_host")

    if not os.path.isdir(user_code_dir):
        os.mkdir(user_code_dir)
    #if not os.path.isfile("/etc/docker/daemon.json"):
    #    with open("/etc/docker/daemon.json", "w") as file:
    #        file.write(json.dumps({"insecure-registries": [registry_host]}))
    #os.system("service docker start && sleep 3")

    client = docker.from_env()
    images = requests.get("http://{}/v2/_catalog".format(registry_host)).json()

    for image in images["repositories"]:
        if image.startswith("ubersite/codeenv/"):
            client.images.pull("{}/{}".format(registry_host, image))

    args = parser.parse_args()
    uvicorn.run("api.app:app", host=args.host, port=args.port, reload=True, env_file=args.env)