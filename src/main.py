from flask import render_template, session, abort, request
from application import app
from application.models.user_model import UserModel
from application import login_manager

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def anti_csrf():
    """
    Protection of CSRF vulnerability.
    Checks that the "token" is saved in the session or returns a
    error 403.
    """
    if request.method == "POST":
        token = session.pop("_csrf_token", None)
        if not token or token != request.form.get("_csrf_token"):
            abort(403)

@login_manager.user_loader
def load_user(user_id):
    return UserModel().get_user(user_id)
