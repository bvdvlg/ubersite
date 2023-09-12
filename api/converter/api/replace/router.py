from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from replace.model import ReplaceBase

replace_router = APIRouter()

@replace_router.post("/replace")
async def service_request(data: ReplaceBase):
    resp = data.replaced()
    if resp is not None:
        return str(resp)
    else:
        return Response('Can\'t replace string', status_code=status.HTTP_400_BAD_REQUEST)
