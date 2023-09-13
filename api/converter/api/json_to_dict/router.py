from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from api.json_to_dict.model import JsonBase

json2dict_router = APIRouter()

@json2dict_router.post("/json2dict")
async def service_request(data: JsonBase):
    resp = data.as_dict()
    if resp is not None:
        return str(resp)
    else:
        return Response('Json is not valid', status_code=status.HTTP_400_BAD_REQUEST)
