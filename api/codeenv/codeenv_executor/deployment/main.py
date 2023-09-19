from io import BytesIO
import uvicorn
import argparse
import os

import docker
client = docker.from_env()

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="Defines the environment of project")
parser.add_argument("-p", "--port", type=int, help="Defines the environment of project")
parser.add_argument("-b", "--build", type=bool, help="Rebuld docker image")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.build:
        for el in os.listdir('api/task_executor/images'):
            print(el)
            response = [line for line in client.images.build(
                path="api/task_executor/", rm=True, tag=el, dockerfile="images/{}/Dockerfile".format(el)
            )]
    uvicorn.run("api.app:app", host=args.host, port=args.port, reload=True)