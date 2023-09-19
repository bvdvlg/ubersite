from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    class Config:
        pass

class CodeExecutorSettings(Settings):
    source_path: str

    class Config:
        env_prefix = "code_executor_"

