from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    class Config:
        pass

BASE_DIRECTORY = Path(__file__).absolute().parent

class DatabaseSettings(Settings):
    prefix: str
    username: str
    passwd: str
    host: str
    port: int
    database_name: str

    @property
    def url(self):
        return "{}://{}:{}@{}:{}/{}".format(self.prefix, self.username, self.passwd, self.host, self.port, self.database_name)

    class Config:
        env_prefix = "postgres_"

class AuthSettings(Settings):
    auth_enabled: bool

    class Config:
        env_prefix = "auth_settings_"

database_settings = DatabaseSettings()
auth_settings = AuthSettings()