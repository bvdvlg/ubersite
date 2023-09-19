from typing import Any
from sqlalchemy.orm import Session
from enum import Enum
from sqlalchemy.exc import IntegrityError, NoResultFound
from .exceptions import TokenNotFoundError, DbExceptionCommon

class Status:
    def __init__(self) -> None:
        self.__code = None
        self.__content = None

    def set_code(self, status):
        self.__code = status

    def set_content(self, content):
        self.__content = content

    def to_dict(self):
        response = {}
        if self.__code and isinstance(self.__code, int):
            response['status_code'] = int(self.__code)
        if self.__content is not None:
            response['content'] = self.__content
        return response

class SafeDbSession(Session):
    def __init__(self, *args, error_response, **kwargs):
        self.error_response = error_response
        super().__init__(*args, **kwargs)

    def __enter__(self):
        return super().__enter__()

    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None:
        response = False
        if type_ and issubclass(type_, DbExceptionCommon):
            self.error_response.status_code = value.CODE
            self.error_response.content = value.MSG
            self.error_response.body = self.error_response.render(value.MSG)
            response = True
        super().__exit__(type_, value, traceback)
        return response