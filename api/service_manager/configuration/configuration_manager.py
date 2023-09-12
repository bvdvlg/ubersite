from enum import Enum
from functools import cached_property
import os
import json
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    class Config:
        pass

BASE_DIRECTORY = Path(__file__).absolute().parent

class ServerSettings(Settings):
    configuration_file : str

    class Config:
        env_prefix = "service_settings_"

    @cached_property
    def __common_service_config(self):
        filename = self.configuration_file
        if not os.path.isfile(filename):
            raise Exception("Not found")
        
        with open(filename, "r") as file:
            return json.load(file)

    @property
    def service_config(self):
        return self.__common_service_config.get("service_config")
    
    @property
    def logger_config(self):
        return self.__common_service_config.get("logger_config")
        
server_settings = ServerSettings()
print(server_settings)
