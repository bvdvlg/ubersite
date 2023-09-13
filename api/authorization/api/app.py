from fastapi import FastAPI

from starlette import status
from starlette.responses import Response
from configuration.settings import database_settings
from api.models import UsersInterface, TokensInterface
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = FastAPI()
engine = create_engine(database_settings.url)

@app.get("/get_user_info")
async def get_user_info(token: str):
    return Response()