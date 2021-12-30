from datetime import datetime, timedelta

import jwt
from decouple import config


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
        pass
