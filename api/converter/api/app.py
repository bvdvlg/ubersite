from fastapi import FastAPI
from api.json_to_dict.router import json2dict_router
from api.replace.router import replace_router

app = FastAPI()
app.include_router(json2dict_router)
app.include_router(replace_router)