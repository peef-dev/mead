# coding: utf-8

from datetime import datetime
from application.tools.helpers import get_code
from application import db
from application.models.user_model import UserModel

CATEGORIES = {
    'thread': 'Thread'
}


class PostModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    content = db.Column(db.Text)
    reference = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.id'),
        nullable=False)
    is_hide = db.Column(db.Boolean)

    images = db.relationship('PhotoModel', backref='photo_model', lazy=True)

    def create(self, **kwargs):
        data = kwargs['data']

        self.reference = get_code() + str(self.id) + str(datetime.now().microsecond)
        self.user_id = int(data.get('user_id'))         
        self.category = CATEGORIES[data.get('category')]
        self.content = data.get('content')

        db.session.add(self)
        db.session.commit()
        return self

    def hide(self, id):
        post = self.query.filter_by(id=id).first()
        post.is_hide = True
        db.session.flush()
        db.session.commit()


