class DbExceptionCommon(Exception):
    pass

class TokenNotFoundError(DbExceptionCommon):
    MSG = "selected token is not found"
    CODE = 400

class UserNotFoundError(DbExceptionCommon):
    MSG = "requested user is not found"
    CODE = 400

class UserAlreadyExists(DbExceptionCommon):
    MSG = "user is already exists"
    CODE = 400

class TokenAlreadyExistsError(DbExceptionCommon):
    MSG = "token is already exists"
    CODE = 400

class RequesterNotFoundError(DbExceptionCommon):
    MSG = "can't identify requester user"
    CODE = 400

class NoPermissionsError(DbExceptionCommon):
    MSG = "user requester don't have right permission"
    CODE = 401

class UnauthorizedError(DbExceptionCommon):
    MSG = "you are not authorized"
    CODE = 401

class IncorrectPasswordError(DbExceptionCommon):
    MSG = "the selected password is incorrect"
    CODE = 401

class UserTokensIntegrityError(DbExceptionCommon):
    MSG = "you can't do this action because user has active tokens"
    CODE = 400