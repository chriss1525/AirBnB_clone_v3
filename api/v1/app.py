#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""initializes a new Flask app"""

# import storage from models
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
import os
<<<<<<< HEAD
<<<<<<< HEAD
import requests
=======
from os import getenv
>>>>>>> ddab3a8ccc69bae4392251f2dc4019c7bf3fc707
=======
from os import getenv
>>>>>>> 3e1910784406a73baa2ef096d8da0e16c6dbec33


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """page_not_found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
