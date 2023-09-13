from fastapi import FastAPI

from starlette import status
from starlette.responses import Response
from configuration.configuration_manager import server_settings
import aiohttp
import json
import logging
from fastapi import Request

service_config = server_settings.service_config
logger_config = server_settings.logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger(__name__)

app = FastAPI()
    
@app.post("/{service_name}")
async def ask_service(request: Request, service_name: str):
    body = await request.body()
    if not service_config.get(service_name):
        return Response('Unknown service', status_code=status.HTTP_400_BAD_REQUEST)
    else:
        async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
            async with session.post("http://{}{}".format(service_config[service_name]["host"], service_config[service_name]["path"]), data=body) as response:
                if response.ok:
                    body = await response.json()
                else:
                    body = None
                text = await response.text()
        if (body):
            return Response(body, status_code=response.status)
        else:
            return Response(text, status_code=response.status)