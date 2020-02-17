"""Service code schemas to assist with service code / plan serialization"""
from marshmallow import fields, Schema


class PlanSchema(Schema):
    """Schema class to handle serialization of plan data"""
    id = fields.String()
    description = fields.String()
    mb_aviliable = fields.Integer()
    is_unlimited = fields.Boolean()


class ServiceCodeSchema(Schema):
    """Schema class to handle serialization of simplified service code data"""
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
