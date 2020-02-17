"""Subscription manager responses for the business logic and
process any subscription requests"""
from src.models.base import db
from src.models.subscriptions import Subscription


class SubscriptionManager:
    """Manager of Subscription model.

    Response for the business logic
    """
    @classmethod
    def get_all_subscriptions(cls, **kwargs):
        """Gets a list of Subscription objects using given kwargs

        Generates query filters from kwargs param using base class method

        Args:
            kwargs: key value pairs to apply as filters

        Returns:
            list: objects returned from query result

        """
        return Subscription.query.filter(**kwargs).all()

    @classmethod
    def get_one(cls, sid):
        """Get Subcription object by id
        Args:
            sid (int): id of subscription object

        Returns:
            object: subscription object or none
        """
        return Subscription.query.get_or_404(sid)

    @classmethod
    def get_all_ids(cls):
        """Gets a list of Subscription ids

        Returns:
            List[int]: list of Subscription ids
        """
        subscriptions = db.session.query(Subscription.id).all()
        return [s.id for s in subscriptions]
