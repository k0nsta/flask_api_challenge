"""Usage related models and database functionality"""
from decimal import Decimal
from src.models.base import db
from src.models.mixins import BaseModel


class DataUsage(BaseModel, db.Model):
    """Model class to represent data usage record

    Note:
        A daily usage record is created for a subscription each day
        it is active, beginning at midnight UTC timezone.

    """
    __tablename__ = "data_usages"

    mb_used = db.Column(db.Float, default=0.0)
    from_date = db.Column(db.TIMESTAMP(timezone=True))
    to_date = db.Column(db.TIMESTAMP(timezone=True))

    subscription_id = db.Column(
        db.Integer, db.ForeignKey("subscriptions.id"), nullable=False
    )
    subscription = db.relationship("Subscription", back_populates="data_usages")

    def __repr__(self):  # pragma: no cover
        return "<{0}: {1} ({2}) {3} MB {4} - {5}>".format(
            self.__class__.__name__,
            self.id,
            self.subscription_id,
            self.mb_used,
            self.from_date,
            self.to_date,
        )
