"""DataUsage manager responses for the business logic related with
data usage, process any data usage requests"""
from sqlalchemy import case
from sqlalchemy import func

from src.models.base import db

from src.models.usages import DataUsage
from src.models.cycles import BillingCycle
from src.models.service_codes import Plan
from src.models.subscriptions import Subscription as S
from src.models.subscriptions import SubscriptionStatus as SEnum
from src.models.service_codes import ServiceCode as SrvCode


class DataUsageManager:

    @classmethod
    def get_current_usage(cls, sid):
        """Get consumed data by current bulling cycle and status

        Args:
            sid (int): id of subscription object

        Returns:
            dict: data returned from query result
        """
        case_stms = case(
            [
                (S.service_codes.any(SrvCode.name == "Data Block"), True),
                (~S.service_codes.any(SrvCode.name == "Data Block"), False),
            ]
        )

        cycle = BillingCycle.get_current_cycle()
        obj = db.session.query(
            S,
            case_stms.label("is_blocked"),
            func.sum(DataUsage.mb_used).label("consumed_data"))\
            .join(DataUsage)\
            .filter(
                S.id == sid,
                DataUsage.from_date >= cycle.start_date,
                DataUsage.to_date <= cycle.end_date)\
            .first()

        return dict(mb_used=obj.consumed_data, is_blocked=obj.is_blocked)

    @classmethod
    def set_service_block_code(cls, sid):
        """Set service code `Data Block` for subscription objects with
        exceeded allowing quota and have any status except `new`

        Args:
            sid (int): id of subscription object
        """
        cycle = BillingCycle.get_current_cycle()
        statuses = [s for s in SEnum if s.value != 'new']
        obj = db.session.query(
            S,
            Plan.is_unlimited.label('unlimited'),
            Plan.mb_available.label('available'),
            func.sum(DataUsage.mb_used).label('consumed_data'))\
            .join(DataUsage, Plan)\
            .filter(
                S.id == sid,
                S.status.in_(statuses),
                DataUsage.from_date >= cycle.start_date,
                DataUsage.to_date <= cycle.end_date)\
            .first()
        if obj.Subscription:
            if obj.unlimited is False and obj.consumed_data > obj.available:
                block_code = db.session.query(SrvCode)\
                    .filter_by(name='Data Block')\
                    .first()
                obj.Subscription.service_codes.append(block_code)
                db.session.commit()




