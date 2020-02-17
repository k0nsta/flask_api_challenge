"""Subscription resource for handling any subscription requests"""
from flask_restful import Resource

from src.managers import SubscriptionManager
from src.schemas import SubscriptionSchema


class SubscriptionAPI(Resource):
    """Resource/routes for subscription endpoints"""

    def get(self, sid):
        """External facing subscription endpoint GET

        Gets an existing Subscription object by id

        Args:
            sid (int): id of subscription object

        Returns:
            json: serialized subscription object

        """
        subscription = SubscriptionManager.get_one(sid)
        result = SubscriptionSchema().dump(subscription)
        return result.data


class SubscriptionListAPI(Resource):
    """Resource/routes for subscriptions endpoints"""

    def get(self, **kwargs):
        """External facing subscription list endpoint GET

        Gets a list of Subscription object with given args

        Args:
            kwargs (dict): filters to apply to query Subscriptions

        Returns:
            json: serialized list of Subscription objects

        """
        subscriptions = SubscriptionManager.get_all_subscriptions(**kwargs)
        result = SubscriptionSchema().dump(subscriptions, many=True)
        return result.data
