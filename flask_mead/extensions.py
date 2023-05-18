from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()


login_manager.login_view = "mead.login"
login_manager.login_message = "Welcome! Please login to acces to app."


@login_manager.user_loader
def load_user(user_id):
    from flask_mead.services import UserService

    user = UserService(db.session)
    return user.get_user_by_id(user_id)
