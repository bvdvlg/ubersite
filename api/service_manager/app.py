from fastapi import FastAPI

from starlette import status
from starlette.responses import Response
from configuration.configuration_manager import ConfigurationManager
from models import Body
import uvicorn
import aiohttp
import json
import logging
import logging

cm = ConfigurationManager("testing")
logging.config.dictConfig(cm["logger_config"])
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/api/service_request")
async def service_request(data: Body):
    service_config = cm["service_config"]
    if not service_config.get(data.service):
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
            async with session.post("http://{}{}".format(service_config[data.service]["host"], service_config[data.service]["path"]), data=json.dumps(data.data)) as response:
                resp = await response.json()
        return resp
    
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)