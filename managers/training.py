from models import BeginnersTrainingModel, AdvancedTrainingModel
from db import db


class TrainingManager:
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
