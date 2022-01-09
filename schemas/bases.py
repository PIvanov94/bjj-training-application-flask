from marshmallow import Schema, fields, validate


class BaseTrainingSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=100))
    starting_time = fields.String(required=True, validate=validate.Length(max=50))
    group = fields.String(required=True, validate=validate.Length(max=50))
    note = fields.String(required=True, validate=validate.Length(max=100))