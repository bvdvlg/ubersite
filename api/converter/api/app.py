from fastapi import FastAPI
from api.json_to_dict.router import json2dict_router
from api.replace.router import replace_router
from fastapi.exceptions import RequestValidationError
from starlette.responses import Response

app = FastAPI()
app.include_router(json2dict_router)
app.include_router(replace_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return Response(str(exc), 400, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    })