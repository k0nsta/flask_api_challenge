"""API route declarations

Imports any Flask resources and registers them as API routes to accept
requests and return responses on the Flask server.
"""
from flask import Blueprint
from flask_restful import Api


def register_routes(_app):
    """Registers api resources/routes with Flask app

    Args:
        _app (object): Flask app object

    """
    from src.resources.subscriptions import (
        SubscriptionAPI,
        SubscriptionListAPI
    )
    from src.resources.usages import DataUsageAPI
    from src.resources.service_codes import PlanAPI, PlanListAPI

    api_blueprint = Blueprint("api", __name__)
    api = Api(api_blueprint, catch_all_404s=False)

    api.add_resource(
        SubscriptionAPI, "/subscription/<int:sid>/", strict_slashes=False)
    api.add_resource(
        SubscriptionListAPI, "/subscriptions/", strict_slashes=False)
    api.add_resource(
        DataUsageAPI, "/subscription/<int:sid>/usage/", strict_slashes=False)
    api.add_resource(
        PlanAPI, "/plan/<int:pid>/", strict_slashes=False)
    api.add_resource(
        PlanListAPI, "/pans/", strict_slashes=False)

    _app.register_blueprint(api_blueprint, url_prefix="/api")
