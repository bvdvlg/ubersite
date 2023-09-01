from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from fastapi import FastAPI
import uvicorn

from api.router import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("router:app", port=8000, reload=True)