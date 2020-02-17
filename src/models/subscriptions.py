"""Subscription related models and database functionality"""
from enum import Enum

from sqlalchemy.dialects.postgresql import ENUM

from src.models.base import db
from src.models.mixins import BaseModel
from src.models.service_codes import subscriptions_service_codes
from src.models.usages import DataUsage


class SubscriptionStatus(Enum):
    """Enum representing possible subscription statuses"""
    new = "new"
    active = "active"
    suspended = "suspended"
    expired = "expired"


class Subscription(BaseModel, db.Model):
    """Model class to represent ATT subscriptions"""

    __tablename__ = "subscriptions"

    phone_number = db.Column(db.String(10))
    status = db.Column(ENUM(SubscriptionStatus), default=SubscriptionStatus.new)

    plan_id = db.Column(db.Integer, db.ForeignKey("plans.id"), nullable=False)
    plan = db.relationship("Plan", foreign_keys=[plan_id], lazy="select")
    service_codes = db.relationship(
        "ServiceCode", secondary=subscriptions_service_codes,
        primaryjoin="Subscription.id==subscriptions_service_codes.c.subscription_id",
        secondaryjoin="ServiceCode.id==subscriptions_service_codes.c.service_code_id",
        back_populates="subscriptions", cascade="all,delete", lazy="subquery"
    )

    data_usages = db.relationship(DataUsage, back_populates="subscription")

    def __repr__(self):  # pragma: no cover
        return "<{0}: {1} ({2}), p_number: {3}, plan: {4}>".format(
            self.__class__.__name__,
            self.id,
            self.status,
            self.phone_number or '[no phone number]',
            self.plan_id
        )
