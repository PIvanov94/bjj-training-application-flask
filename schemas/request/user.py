from marshmallow import Schema, fields, validate

from util.helpers import validate_password


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(
        required=True,
        validate=validate.And(validate.Length(min=6, max=255), validate_password),
    )


class StudentLoginRequestSchema(BaseUserSchema):
    pass


class CoachLoginRequestSchema(BaseUserSchema):
    pass


class StudentRegisterRequestSchema(BaseUserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=12))
    belt = fields.String(validate=validate.Length(max=255))