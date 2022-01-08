from models import BeginnersTrainingModel, AdvancedTrainingModel
from db import db


class TrainingManager:
    """TODO: Make the logic for creating trainings for advanced and beginners groups"""
    @staticmethod
    def create(training_data, coach):
        training_data["coach_id"] = coach.id
        training = BeginnersTrainingModel(**training_data)
        db.session.add(training)
        db.session.flush()
        return training
