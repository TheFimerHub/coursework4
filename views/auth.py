from flask import request
from flask_restx import Namespace, Resource
from container import auth_service
from container import user_service

auth_ns = Namespace("auth")


@auth_ns.route('/login/')
class AuthView(Resource):

    def post(self):
        req_json = request.json
        if None in [req_json.get('email', None), req_json.get('password', None)]:
            return '', 400
        tokens = auth_service.generate_token(req_json.get('email'), req_json.get('password'))
        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token', None)

        if refresh_token is None:
            return '', 401

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201


@auth_ns.route('/register/')
class AuthViewRegister(Resource):

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return '', 201
