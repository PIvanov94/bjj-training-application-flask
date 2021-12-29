from marshmallow import Schema, fields, validate, ValidationError
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
        raise ValidationError(f"Your password must have at least one uppercase letter,"
                              f" number and one special character")


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.And(validate.Length(min=6, max=255), validate_password))


class StudentRegisterSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=12))
    belt = fields.String(validate=validate.Length(max=255))

