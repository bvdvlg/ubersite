from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    class Config:
        pass

class CodeenvExecutorSettings(Settings):
    user_code_dir: str
    lib_code_dir: str
    user_code_mountpoint: str
    lib_code_mountpoint: str
    repository: str

    class Config:
        env_prefix = "code_executor_"

codeenv_executor_settings = CodeenvExecutorSettings()