from werkzeug.exceptions import NotFound

from managers.auth import auth
from models import BeginnersTrainingModel, AdvancedTrainingModel
from db import db


class TrainingManager:

    @staticmethod
    def get_all():
        return BeginnersTrainingModel.query.all()

    @staticmethod
    def create(training_data, coach):
        training_data["coach_id"] = coach.id
        group = training_data["group"]

        if group == "beginners":
            training = BeginnersTrainingModel(**training_data)
            db.session.add(training)
            db.session.commit()
        elif group == "advanced":
            training = AdvancedTrainingModel(**training_data)
            db.session.add(training)
            db.session.commit()
        return training

    @staticmethod
    def update(training_data, id_):
        group = training_data["group"]
        # Check the following code for working!
        if group == "beginners":
            training_query = BeginnersTrainingModel.query.filter_by(id=id_)
            training = training_query.first()
            if not training:
                raise NotFound("There is no such training")

            user = auth.current_user()

            if not user.id == training.coach_id:
                raise NotFound("You do not have access to make changes to this training")
            training_query.update(training_data)
            db.session.add(training)
            db.session.flush()
        elif group == "advanced":
            training_query = BeginnersTrainingModel.query.filter_by(id=id_)
            training = training_query.first()
            if not training:
                raise NotFound("There is no such training")

            user = auth.current_user()

            if not user.id == training.coach_id:
                raise NotFound("You do not have access to make changes to this training")
            training_query.update(training_data)
            db.session.add(training)
            db.session.flush()
        return training