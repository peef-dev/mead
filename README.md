# Flask-Mead

## !!! WORK IN PROGRESS !!!

Flask-Mead is a Flask extension that let's you build custom components for your web application.
It includes:

- PostgreSQL support
- Basic users authentication

## Example

```
from flask import Flask
from flask_mead import Mead

app = Flask(__name__)

mead_app = Mead()
mead_app.init_app(app)
```

This extension is in active development and not ready yet, use it only for testing purposes.
