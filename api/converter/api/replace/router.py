from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from api.replace.model import ReplaceBase
import json

replace_router = APIRouter()

@replace_router.options("/replace")
async def options_request():
    return Response(status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
        }
    )

@replace_router.post("/replace")
async def service_request(data: ReplaceBase):
    resp = data.replaced()
    if resp is not None:
        return Response(json.dumps({"body": str(resp)}), headers={"Access-Control-Allow-Origin": "*"})
    else:
        return Response('Can\'t replace string', status_code=status.HTTP_400_BAD_REQUEST)
