# coding: utf-8

from application import db

# Storing images into postgresql
# https://stackoverflow.com/questions/54500/storing-images-in-postgresql
# https://kb.objectrocket.com/postgresql/upload-image-with-python-to-postgres-1110
# https://www.postgresqltutorial.com/postgresql-python/blob/
# https://stackoverflow.com/questions/24933784/one-to-one-relationship-in-flask


class PhotoModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    image_url  = db.Column(db.String(64))
    blob_key = db.Column(db.LargeBinary)
    alt = db.Column(db.String(64))

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.id'),
        nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.id'),
        nullable=False)

    def create(self, **kwargs):
        data = kwargs['data']
        self.image_url = data.get('image_url')
        self.blob_key = data.get('blob_key')
        self.alt = data.get('alt')
        self.article_key = data.get('article_key')
        self.put()
