from pydantic import BaseModel, HttpUrl
import json
import re

class ReplaceBase(BaseModel):
    data: str
    filter_regexp: str
    replace_text: str

    def replaced(self):
        all_phrases = set(re.findall(self.filter_regexp, self.data))
        result = self.data
        for el in all_phrases:
            result = result.replace(el, self.replace_text)
        return result