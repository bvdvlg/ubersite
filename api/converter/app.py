from fastapi import FastAPI
from json_to_dict.router import json2dict_router
from replace.router import replace_router
import uvicorn

app = FastAPI()
app.include_router(json2dict_router)
app.include_router(replace_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)