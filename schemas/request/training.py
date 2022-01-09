from marshmallow import Schema, fields, validate

from schemas.bases import BaseTrainingSchema


class TrainingCreateRequestSchema(BaseTrainingSchema):
    photo = fields.String(required=True)
    photo_extension = fields.String(required=True)