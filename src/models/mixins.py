from src.models.base import db


class BaseModel:
    """Model Base class contains id field"""
    id = db.Column(db.Integer, primary_key=True)