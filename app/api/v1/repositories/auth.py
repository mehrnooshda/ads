from flask import jsonify, g, request, Response
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models.user import User
from app.services.app_exceptions import CustomException, InputValidationError, AuthenticationException
from app.services.token_helper import generate_token
from app.utils import validate_email


def register():
    action = 'REGISTER'
    try:
        request_body = request.get_json()
    except Exception as e:
        raise CustomException('invalid request.{}'.format(e), 406)
    username = request_body['username']
    password = request_body['password']
    if validate_email(username):
        try:
            user = User(username=username, hashed_password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            raise CustomException(' {}:ثبت نام با موفقیت انجام نشد.'.format(e), 406)

    return jsonify({"result": {
        "message": "registered!"}})


def login():
    log_action = "LOGIN"
    try:
        request_body = request.get_json()
    except Exception as e:
        raise CustomException('invalid request.{}'.format(e), 406)

    if 'username' not in request_body or 'password' not in request_body:
        raise InputValidationError()
    username = request_body['username']
    password = request_body['password']

    user_obj = User.query \
        .filter(User.username == request_body['username']) \
        .first()

    if not user_obj:
        raise AuthenticationException()

    if not check_password_hash(user_obj.hashed_password, password):
        message = "Username or password is not correct"
        raise AuthenticationException(message=message)

    else:
        return Response(
            response="Successfully logged in",
            headers={'Authorization': "Bearer " + generate_token(username),
                     'access-control-expose-headers': '*'},
            mimetype='application/json'
        )

