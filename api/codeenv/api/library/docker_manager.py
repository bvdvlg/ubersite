from typing import Any
import docker
import requests



class DockerContainerModule(dict):
    def __init__(self, client, **kwargs):
        self.client = client
        self.running_container = None
        super().__init__(**kwargs)

    def add_mount(self, mount):
        if not self.get("mounts"):
            self["mounts"] = []
        self["mounts"].append(mount)
        return self

    def _find_env_key(self, key):
        env = self.get("environment")
        if env is None:
            return None
        for i in range(len(env)):
            splitted = env[i].split("=")
            if len(splitted) != 2:
                continue
            if splitted[0] == key:
                return i
        return None

    def add_environment_var(self, key, value):
        if not self.get("environment"):
            self["environment"] = []
        if self._find_env_key(key) is not None:
            self["environment"][self._find_env_key(key)] = "{}={}".format(key, value)
        else:
            self["environment"].append("{}={}".format(key, value))
        return self
    
    def append_environment_var(self, key, value):
        if not self.get("environment"):
            self["environment"] = []
        env = self["environment"]
        if self._find_env_key(key) is not None:
            env[self._find_env_key(key)] = "{}:{}".format(env[self._find_env_key(key)], value)
        else:
            self.add_environment_var(key, value)
        return self

    def set_image(self, image):
        self["image"] = self.client.images.get(image)
        return self
    
    def run(self):
        self.running_container = self.client.containers.run(**self)
        return self.running_container

    def wait(self, timeout):
        if self.running_container is None:
            return
        return self.running_container.wait(timeout=timeout)
    
    def check_stderr(self):
        if self.running_container is None:
            return
        return self.running_container.logs(stdout=False, stderr=True).decode("utf-8")
    
    def check_stdout(self):
        if self.running_container is None:
            return
        return self.running_container.logs(stdout=True, stderr=False).decode("utf-8")
    
    def clear(self):
        if self.running_container is None:
            return
        try:
            self.running_container.kill()
        except docker.errors.NotFound:
            pass
        except docker.errors.APIError:
            pass
        self.running_container.remove()


class DockerContainerExecutorWrapper:
    def __init__(self, docker_client, error_response, **kwargs) -> None:
        self.error_response = error_response
        self.container = DockerContainerModule(docker_client, **kwargs)
    def __enter__(self):
        return self.container
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None:
        response = False
        if type_ == docker.errors.ImageNotFound:
            self.error_response.status_code = 400
            self.error_response.content = "This image isn't exists"
            self.error_response.body = self.error_response.render(self.error_response.content)
            response = True
        elif type_ == requests.exceptions.ConnectionError:
            self.error_response.status_code = 408
            self.error_response.content = "Code is executing too long"
            self.error_response.body = self.error_response.render(self.error_response.content)
            response = True
        self.container.clear()
        return response