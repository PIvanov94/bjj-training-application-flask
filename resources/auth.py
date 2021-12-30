from flask import request
from flask_restful import Resource

from managers.auth import AuthManger
from managers.user import UserManager
from schemas.request.user import StudentRegisterSchema
from util.decorators import validate_schema


class Register(Resource):
    @validate_schema(StudentRegisterSchema)
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManger.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    def post(self):
        pass


class LoginCoach(Resource):
    def post(self):
        pass
