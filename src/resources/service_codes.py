"""Plan resource for handling any plan requests"""
from flask_restful import Resource

from src.models.service_codes import Plan
from src.schemas import PlanSchema


class PlanAPI(Resource):
    """Resource/routes for plan endpoints"""

    def get(self, pid):
        """External facing plan endpoint GET

        Gets an existing Plan object by id

        Args:
            pid (int): id of plan object

        Returns:
            json: serialized plan object

        """
        plan = Plan.query.get_or_404(pid)
        result = PlanSchema().dump(plan)
        return result.data


class PlanListAPI(Resource):
    """Resource/routes for plans endpoints"""

    def get(self, **kwargs):
        """External facing plan list endpoint GET

        Gets a list of Plan object with given args

        Args:
            kwargs (dict): filters to apply to query Plan

        Returns:
            json: serialized list of Plan objects

        """
        plans = Plan.query.filter_by(**kwargs).all()
        result = PlanSchema().dump(plans, many=True)
        return result.data
