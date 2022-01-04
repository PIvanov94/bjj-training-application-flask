from sqlalchemy import func
from db import db
from models.enums import State


class BaseTrainingModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    starting_time = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)


class BeginnersTrainingModel(BaseTrainingModel):
    pass


class AdvancedTrainingModels(BaseTrainingModel):
    pass

