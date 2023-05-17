export FLASK_APP=app.py
export FLASK_DEBUG=1
flask db migrate
flask db upgrade
