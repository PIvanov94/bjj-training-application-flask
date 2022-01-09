from marshmallow import fields, validate

from schemas.bases import BaseTrainingSchema


class TrainingCreateResponseSchema(BaseTrainingSchema):
    id = fields.Integer(required=True)
    photo_url = fields.String(required=True, validate=validate.Length(max=255))