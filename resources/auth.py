from flask import request
from flask_restful import Resource

from managers.auth import AuthManger
from managers.user import UserManager, AdminManager, CoachManager
from schemas.request.user import StudentRegisterRequestSchema, StudentLoginRequestSchema, CoachLoginRequestSchema, \
    AdminLoginRequestSchema
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
    @validate_schema(CoachLoginRequestSchema)
    def post(self):
        user = CoachManager.login(request.get_json())
        token = AuthManger.encode_token(user)
        return {"token": token}, 200


class LoginAdmin(Resource):
    @validate_schema(AdminLoginRequestSchema)
    def post(self):
        admin = AdminManager.login(request.get_json())
        token = AuthManger.encode_token(admin)
        return {"token": token}, 200