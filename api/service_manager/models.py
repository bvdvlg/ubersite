from pydantic import BaseModel, HttpUrl

class Body(BaseModel):
    service: str
    data: dict