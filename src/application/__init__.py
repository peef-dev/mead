__version__ = '1.0.0'



import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_sslify import SSLify

from application.tools import date_time, security
from application.config import SECRET_KEY, DATABASE_URI


app = Flask(
    __name__, 
    instance_relative_config=True,
    static_url_path='',
    template_folder='views'
)

# CONFIGURATIONS
app.config["SECRET_KEY"] = SECRET_KEY
app.jinja_env.globals["csrf_token"] = security.generate_token
app.jinja_env.filters["format_date_time"] = date_time.format_date
app.jinja_env.globals["dev_mode"] = os.environ.get('SERVER_SOFTWARE','').startswith('Development')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

# FLASK EXTENSIONS
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
#sslify = SSLify(app)
login_manager.login_view = "login"
login_manager.login_message = "Bienvenue"

# LOAD CONTROLLERS
from application.controllers import *
