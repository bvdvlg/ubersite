from pydantic import BaseModel, HttpUrl
import json
import re

class PythonCode(BaseModel):
    code: str
    image: str
    library: str = None