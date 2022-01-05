from datetime import datetime, timedelta
from flask_httpauth import HTTPTokenAuth
import jwt
from decouple import config
from werkzeug.exceptions import BadRequest
from models.user import StudentModel, CoachModel, AdminModel

role_models = [StudentModel, CoachModel, AdminModel]


class AuthManger:
    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=100),
            "role": user.__class__.__name__,
        }
        return jwt.encode(payload, key=config("JWT_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        try:
            data = jwt.decode(token, key=config("JWT_KEY"), algorithms=["HS256"])
            return data["sub"], data["role"]
        except jwt.ExpiredSignatureError:
            raise BadRequest("Expired token")
        except jwt.InvalidTokenError:
            raise BadRequest("Invalid token")


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    user_id, role = AuthManger.decode_token(token)
    user = eval(f"{role}.query.filter_by(id={user_id}).first()")
    return user
