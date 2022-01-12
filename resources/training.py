from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.training import TrainingManager
from models import RoleType
from schemas.request.training import TrainingCreateRequestSchema
from schemas.response.training import TrainingCreateResponseSchema
from util.decorators import validate_schema, permission_required


class ListCreateTraining(Resource):
    """TODO: Make possible to show all trainings (beginners ana advanced classes)"""
    @auth.login_required
    def get(self):
        trainings = TrainingManager.get_all()
        schema = TrainingCreateResponseSchema()
        return schema.dump(trainings, many=True)

    @auth.login_required
    @permission_required(RoleType.coach)
    @validate_schema(TrainingCreateRequestSchema)
    def post(self):
        current_user = auth.current_user()
        training = TrainingManager.create(request.get_json(), current_user)
        schema = TrainingCreateResponseSchema()
        return schema.dump(training), 201


class TrainingDetail(Resource):
    @auth.login_required
    @permission_required(RoleType.coach)
    @validate_schema(TrainingCreateRequestSchema)
    def put(self, id_):
        updated_training = TrainingManager.update(request.get_json(), id_)
        schema = TrainingCreateRequestSchema()
        return schema.dump(updated_training)

    @auth.login_required
    @permission_required(RoleType.coach)
    def delete(self, id_):
        pass


class BeginnersJoinTraining(Resource):
    @auth.login_required
    @permission_required(RoleType.student)
    def put(self, id_):
        training = TrainingManager.join_student(id_)
        schema = TrainingCreateResponseSchema()
        return schema.dump(training)