from marshmallow import Schema, fields, validate


class TrainingCreateRequestSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=100))
    starting_time = fields.String(required=True, validate=validate.Length(max=50))
    note = fields.String(required=True, validate=validate.Length(max=100))
    photo_url = fields.String(required=True, validate=validate.Length(max=255))