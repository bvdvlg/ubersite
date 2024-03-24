import docker
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--registry", type=str, help="Docker registry url")

client = docker.from_env()

if __name__ == "__main__":
    args = parser.parse_args()
    for el in os.listdir('api/task_executor/images'):
        tag = "{}/executor_lib_{}".format(args.registry, el)
        response = [line for line in client.images.build(
            path="api/task_executor/", rm=True, tag=tag, dockerfile="images/{}/Dockerfile".format(el)
        )]
        response = client.images.push(tag)