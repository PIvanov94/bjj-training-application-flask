from marshmallow import ValidationError
from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    uppercase=1,
    numbers=1,
    special=1,
    nonletters=1,
)


def validate_password(password):
    errors = policy.test(password)
    if errors:
        raise ValidationError(
            f"Your password must have at least one uppercase letter,"
            f" number and one special character"
        )
