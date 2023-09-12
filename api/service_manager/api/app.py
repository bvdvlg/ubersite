from fastapi import FastAPI

from starlette import status
from starlette.responses import Response
from configuration.configuration_manager import server_settings
from api.models import Body
import aiohttp
import json
import logging
import logging

service_config = server_settings.service_config
logger_config = server_settings.logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/api/service_request")
async def service_request(data: Body):
    if not service_config.get(data.service):
        return Response('Unknown service', status_code=status.HTTP_400_BAD_REQUEST)
    else:
        async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
            async with session.post("http://{}{}".format(service_config[data.service]["host"], service_config[data.service]["path"]), data=json.dumps(data.data)) as response:
                resp = await response.json()
        return Response(resp, status_code=status.HTTP_200_OK)