from flaskext.sqlalchemy import SQLAlchemy
from mead import app

__version__ = '0.0.0'

db = SQLAlchemy(app)


class Page(db.Model):
    """The :class:`Page` object is a Page.
    """
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True)
    slug = db.Column(db.Text, unique=True)
    content = db.Column(db.Text)
    type = db.Column(db.Text)

    def __repr__(self):
        return '<Page #%r>' % self.id



class Post(db.Model):
    """The :class:`Post` object is a Post .
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.Text, unique=True)
    title = db.Column(db.Text, unique=True)
    content = db.Column(db.Text)
    type = db.Column(db.Text)

    def __repr__(self):
        return '<Post #%r>' % self.id

# meta class page
# meta class post
