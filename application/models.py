from datetime import datetime

from flask_login import UserMixin

from application.extensions import db


class BaseModel:
    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model, BaseModel, UserMixin):
    """This class is the user entity.

    It inherit from UserMixin so it can contain default implementations
    for the methods that Flask-Login expects user objects to have.
    """

    name = db.Column(db.String(64), index=True)
    identifier = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

    role = db.relationship("Role", backref="users")


class Role(db.Model, BaseModel):
    name = db.Column(db.String, unique=True, index=True)
    description = db.Column(db.String)
