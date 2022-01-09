from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.user import UserManager
from models import RoleType
from schemas.request.user import RequestCreateAdminSchema, RequestCreateCoachSchema
from util.decorators import permission_required, validate_schema


class CreateAdmin(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(RequestCreateAdminSchema)
    def post(self):
        data = request.get_json()
        UserManager.create_admin(data)
        return 201


class CreateCoach(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(RequestCreateCoachSchema)
    def post(self):
        data = request.get_json()
        UserManager.create_coach(data)
        return 201
