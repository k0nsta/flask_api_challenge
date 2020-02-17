"""DataUsage schemas to assist with sub serialization"""
from marshmallow import fields, Schema, post_dump

# from src.schemas.service_codes import PlanSchema
# from src.schemas.subscriptions import SubscriptionSchema


class DataUsageSchema(Schema):
    """Schema class to handle serialization of data usage"""
    id = fields.Integer()

    mb_used = fields.Float(dump_to="gb_used")
    is_blocked = fields.Boolean()

    @post_dump
    def postpocess(self, in_data):
        """Convert Mb to Gb for representation

        Args:
            in_data (dict): serializer object

        Returns:
            dict: serializer data
        """
        mb = in_data.get("gb_used", 0.0)
        if mb:
            one_gb = 1024
            in_data["gb_used"] = mb / one_gb
        return in_data
