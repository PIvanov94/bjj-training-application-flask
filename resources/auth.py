from flask import request
from flask_restful import Resource

from managers.auth import AuthManger
from managers.user import UserManager
from schemas.request.user import StudentRegisterRequestSchema, StudentLoginRequestSchema
from util.decorators import validate_schema


class Register(Resource):
    @validate_schema(StudentRegisterRequestSchema)
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManger.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    @validate_schema(StudentLoginRequestSchema)
    def post(self):
        user = UserManager.login(request.get_json())
        token = AuthManger.encode_token(user)
        return {"token": token}, 200


class LoginCoach(Resource):
    def post(self):
        pass
