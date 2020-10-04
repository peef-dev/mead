# coding: utf-8

from datetime import datetime
from flask_login import UserMixin
from application import db
from werkzeug.security import generate_password_hash

class UserModel(db.Model, UserMixin):
    """This class is the user entity. It inherit from UserMixin so it can
    contain default implementations for the methods that Flask-Login expects
    user objects to have."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64))
    password = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    active = db.Column(db.Boolean)
    cgu_accepted = db.Column(db.Boolean)
    is_admin = db.Column(db.Boolean)

    posts = db.relationship('PostModel', backref='user_model', lazy=True)
    profile_photo = db.relationship("PhotoModel", uselist=False, backref="user_model")

    def create(self, **kwargs):
        data = kwargs['data']
        
        self.fullname = data.get('fullname')
        self.username = data.get('username')
        self.address = data.get('address')
        self.email = data.get('email')
        self.password = generate_password_hash(data.get('password'))
        self.is_admin = data.get('is_admin')

        if data.get('cgu_accepted') == 'on':
            self.active = True
            self.cgu_accepted = True

        db.session.add(self)
        db.session.commit()
        return self

    def update(self, id, **kwargs):
        pass

    def reset_password(self, id, new_password):
        pass

    def delete(self, id):
        pass

    def activate(self, id):
        pass

    def deactivate(self, id):
        pass

    def get_all_users(self):
        pass

    def get_user(self, user_id):
        return self.query.filter_by(id = user_id).first()

    def get_id(self):
        return self.id
