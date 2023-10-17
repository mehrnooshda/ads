import traceback
from flask import Flask, g, jsonify, request, Response
from werkzeug.exceptions import HTTPException


from app.extensions import ma, db, migrate
from app.api.v1 import api as api_v1
import config
from app.services.app_exceptions import CustomException
from app.api.v1.repositories.healthz import ads_health_check

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['JSON_AS_ASCII'] = False
    app.config['SECRET_KEY'] = 'any secret string'
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/healthz", methods=["GET"])
    def health_checking():
        return ads_health_check()

    @app.errorhandler(CustomException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @api_v1.after_request
    def set_auth_header(response):
        response.headers['Access-Control-Expose-Headers'] = "Authorization"

        new_token = g.get('new_token', None)
        token_payload = g.get('token_payload', None)

        if new_token:
            response.headers['Authorization'] = new_token
            g.new_token = None

        if token_payload:
            response.headers['Is-Guest'] = token_payload['is_guest']

        response.headers['Cache-Control'] = 'no-cache'

        prefix = 'api_v3.'
        endpoint = request.endpoint.replace(prefix, '')
        # if endpoint in openapi:
        #     response.headers['Is-Open-Api'] = True
        return response

    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app
