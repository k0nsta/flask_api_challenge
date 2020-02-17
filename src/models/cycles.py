"""Cycle related models and database functionality"""
from datetime import datetime

from src.models.base import db
from src.models.mixins import BaseModel


class BillingCycle(BaseModel, db.Model):
    """Model class to represent billing cycle dates"""

    __tablename__ = "billing_cycles"

    start_date = db.Column(db.TIMESTAMP(timezone=True))
    end_date = db.Column(db.TIMESTAMP(timezone=True))

    def __repr__(self):  # pragma: no cover
        return "<{0}: {1}, start_date: {2}, end_date: {3}>".format(
            self.__class__.__name__,
            self.id,
            self.id,
            self.end_date
        )

    @classmethod
    def get_current_cycle(cls, date=None):
        """Helper method to get current billing cycle of given date

        Args:
            date (date): date to get billing cycle for

        Returns:
            object: billing cycle object, if any

        """
        if not date:
            date = datetime.now()
        return cls.query.filter(
            cls.start_date <= date, cls.end_date > date).first()
