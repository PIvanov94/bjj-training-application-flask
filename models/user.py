from db import db
from models.enums import RoleType


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class StudentModel(BaseUserModel):
    __tablename__ = "students"

    belt = db.Column(db.String(255))
    role = db.Column(db.Enum(RoleType), default=RoleType.student, nullable=False)


class CoachModel(BaseUserModel):
    __tablename__ = "coaches"

    belt = db.Column(db.String(255))
    role = db.Column(db.Enum(RoleType), default=RoleType.coach, nullable=False)


class AdminModel(BaseUserModel):
    __tablename__ = "administrators"

    role = db.Column(db.Enum(RoleType), default=RoleType.admin, nullable=False)
