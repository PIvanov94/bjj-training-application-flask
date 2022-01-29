from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.user import StudentModel, CoachModel, AdminModel


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = StudentModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest(
                    "This email address is already registered. Please login."
                )
            else:
                raise InternalServerError(
                    "Server is unavailable at the moment. Try again later."
                )
        return user

    @staticmethod
    def create_admin(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = AdminModel(**user_data)
        try:
            db.session.add(user)
            db.session.flush()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest(
                    "This user is already authorized as administrator."
                )
            else:
                raise InternalServerError(
                    "Server is unavailable at the moment. Try again later."
                )
        return user

    @staticmethod
    def create_coach(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = CoachModel(**user_data)
        try:
            db.session.add(user)
            db.session.flush()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest(
                    "This user is already authorized as coach."
                )
            else:
                raise InternalServerError(
                    "Server is unavailable at the moment. Try again later."
                )
        return user

    @staticmethod
    def login(user_data):
        user = StudentModel.query.filter_by(email=user_data["email"]).first()
        if not user or not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")
        return user


class AdminManager:
    @staticmethod
    def login(user_data):
        admin = AdminModel.query.filter_by(email=user_data["email"]).first()
        if not admin or not check_password_hash(admin.password, user_data["password"]):
            raise BadRequest("Wrong email or password")
        return admin


class CoachManager:
    @staticmethod
    def login(user_data):
        user = CoachModel.query.filter_by(email=user_data["email"]).first()
        if not user or not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")
        return user
