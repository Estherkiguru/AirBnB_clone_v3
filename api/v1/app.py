#!/usr/bin/python3
"""
Creates Flask app
Registers app_views blueprint to Flask app
"""

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


flaskapp = Flask(__name__)

flaskapp.register_blueprint(app_views)


if __name__ == '__main__':
    HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    PORT = int(getenv("HBNB_API_PORT", "5000"))
    flaskapp.run(host=HOST, port=PORT, threaded=True)
