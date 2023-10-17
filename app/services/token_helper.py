import datetime
import jwt
import config
from flask import request


def generate_token(username):
    jwt_auth_token = jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=int(config.AUTH_EXP_TIME))
        },
        config.JWT_SECRET_KEY, 'HS256'
    )
    return jwt_auth_token


def decode_token(token):
    decoded_token = jwt.decode(token, config.JWT_SECRET_KEY, 'HS256')
    return decoded_token

