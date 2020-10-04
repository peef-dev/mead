# Mead

If you want to begin a new Flask project, just use it!

This template already contains user register/login functions.

## Manual installation on Ubuntu

```
# Update and install dependencies

sudo apt update
sudo apt install python3 python3-dev python3-venv python3-pip
python3 -m venv lib
. lib/bin/activate
pip install -r requirements.txt

# Initialize environment

. lib/bin/activate
cd src
export FLASK_APP=main.py
export FLASK_ENV=development

# DB migrations

flask db init
flask db migrate
flask db upgrade

# Launch the application

flask run

# Connect to PSQL

sudo -u postgres psql
```
