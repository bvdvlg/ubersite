from functools import wraps
from fastapi import FastAPI

from starlette.responses import Response
from starlette.requests import Request
from configuration.settings import database_settings, auth_settings
from api.models import UsersInterface, TokensInterface
from sqlalchemy import create_engine
from api.library.session import SafeDbSession
from api.library.exceptions import *
import json
from sqlalchemy.exc import IntegrityError, NoResultFound

app = FastAPI()
engine = create_engine(database_settings.url)

def user_from_token(sess, token: str):
    try:
        user_id = sess.query(TokensInterface).filter(TokensInterface.token == token).one().user_id
        user = sess.query(UsersInterface).filter(UsersInterface.id == user_id).one()
    except NoResultFound:
        raise TokenNotFoundError
    return user

def user_from_logpass(sess, login, passwd):
    try:
        user = sess.query(UsersInterface).filter(UsersInterface.login == login).one()
    except NoResultFound:
        raise UserNotFoundError
    if user.passwd != passwd:
        raise IncorrectPasswordError
    return user

def check_action_allowed(login, requester_user):
    return not auth_settings.auth_enabled or login == requester_user.login

def database_interaction(auth_required=False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            error_response = Response(status_code=0)
            for el in ['status', 'sess']:
                if el in kwargs:
                    kwargs.pop(el)
            with SafeDbSession(error_response=error_response, bind=engine) as sess:
                with sess.begin():
                    requester_user = None
                    if kwargs.get('request'):
                        headers = kwargs['request'].headers
                        if headers.get('login') and headers.get('passwd'):
                            requester_user = user_from_logpass(sess, headers['login'], headers['passwd'])
                        elif headers.get('auth_token'):
                            requester_user = user_from_token(sess, headers['auth_token'])
                    if auth_required:
                        if auth_settings.auth_enabled and requester_user is None:
                            raise UnauthorizedError
                        elif requester_user is None:
                            kwargs['requester_user'] = requester_user
                    kwargs['sess'] = sess
                    response = await func(*args, **kwargs)
            if error_response.status_code:
                return error_response
            else:
                return response
        return wrapper
    return decorator

@app.get("/user_info")
@database_interaction(False)
async def get_user_info(token: str, sess=None):
    user = user_from_token(sess, token)
    return Response(user.serialize(), 200)
 
@app.get("/keys")
@database_interaction(True)
async def get_token_keys(request: Request, login: str, sess=None, requester_user=None):
    try:
        user = sess.query(UsersInterface).filter(UsersInterface.login == login).one()
    except NoResultFound:
        raise UserNotFoundError
    if not check_action_allowed(login, requester_user):
        raise NoPermissionsError
    tokens = [el.key for el in user.tokens]
    return Response(json.dumps(tokens), 200)
    
@app.delete("/remove_user")
@database_interaction(True)
async def remove_user(request: Request, login: str, sess=None, requester_user=None):
    try:
        user = sess.query(UsersInterface).filter(UsersInterface.login == login).one()
    except NoResultFound:
        raise UserNotFoundError
    if len(user.tokens) != 0:
        raise UserTokensIntegrityError
    if not check_action_allowed(user.login, requester_user):
        raise NoPermissionsError
    sess.query(UsersInterface).filter(UsersInterface.login == login).delete()
    return Response(status_code=200)

@app.delete("/remove_token")
@database_interaction(False)
async def remove_token(token: str, sess=None):
    try:
        user = sess.query(TokensInterface).filter(TokensInterface.token == token).one()
    except NoResultFound:
        raise TokenNotFoundError
    sess.query(TokensInterface).filter(TokensInterface.token == token).delete()
    return Response(status_code=200)

@app.post("/add_token")
@database_interaction(True)
async def add_token(request: Request, login: str, key: str, token: str, sess=None, requester_user=None):
    if not check_action_allowed(login, requester_user):
        raise NoPermissionsError
    try:
        user_id = sess.query(UsersInterface).filter(UsersInterface.login == login).one().id
        sess.add(TokensInterface(token=token, user_id=user_id, key=key))
        sess.flush()
    except NoResultFound:
        raise UserNotFoundError
    except IntegrityError:
        sess.rollback()
        raise TokenAlreadyExistsError
    return Response(status_code=200)

@app.post("/add_user")
@database_interaction(False)
async def add_user(login: str, email: str, passwd: str, sess=None):
    usr = UsersInterface(login=login, email=email, passwd=passwd)
    try:
        sess.add(usr)
        sess.flush()
    except IntegrityError:
        sess.rollback()
        raise UserAlreadyExists
    return Response(status_code=200)