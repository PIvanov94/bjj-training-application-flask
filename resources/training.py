from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.training import TrainingManager
from models import RoleType
from schemas.request.training import TrainingCreateRequestSchema
from util.decorators import validate_schema, permission_required


class ListCreateTraining(Resource):
    def get(self):
        pass

    @auth.login_required
    @permission_required(RoleType.coach)
    @validate_schema(TrainingCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        training = TrainingManager.create(request.get_json(), current_user)
        schema = TrainingCreateRequestSchema()
        return schema.dump(training), 201