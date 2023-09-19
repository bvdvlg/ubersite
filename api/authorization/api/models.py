from db.schema import Tokens, Users
import json

class UsersInterface(Users):
    pass

    def serialize(self):
        return json.dumps({
            "login": self.login,
            "email": self.email
        })

class TokensInterface(Tokens):
    pass

    def serialize(self):
        return json.dumps({
            "key": self.key,
            "token": self.token
        })