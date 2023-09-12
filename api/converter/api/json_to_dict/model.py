from pydantic import BaseModel, HttpUrl
import json

class JsonBase(BaseModel):
    data: str

    def as_dict(self):
        try:
            return json.loads(self.data)
        except ValueError:
            None