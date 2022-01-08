from db import db


class BaseTrainingModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    starting_time = db.Column(db.String(50), nullable=False)
    note = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    # participants_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    participants = db.Column(db.Text)


class BeginnersTrainingModel(BaseTrainingModel):
    __tablename__ = "beginners"

    coach_id = db.Column(db.Integer, db.ForeignKey("coaches.id"))
    coach = db.relationship("CoachModel")


class AdvancedTrainingModel(BaseTrainingModel):
    __tablename__ = "advanced"

    coach_id = db.Column(db.Integer, db.ForeignKey("coaches.id"))
    coach = db.relationship("CoachModel")

