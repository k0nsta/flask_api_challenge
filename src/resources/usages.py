"""Usage resource for handling any quota requests"""
from flask_restful import Resource

from src.schemas import DataUsageSchema
from src.managers.subsriptions import SubscriptionManager

class  DataUsageAPI(Resource):
    """Data usage for given subscription endpoints"""

    def get(self, sid):
        """External facing Cycle data quota endpoint GET

        Gets used data for given subscription by subscription id

        Args:
            sid (int): id of subscription object

        Returns:x
            json: serialized data usage object
        """

        data = SubscriptionManager.get_current_usage(sid)
        result = DataUsageSchema().dump(data)
        return result.data
