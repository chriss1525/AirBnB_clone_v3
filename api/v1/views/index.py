#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""initializes a new route"""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns a JSON: "status": "OK" """
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    for key, value in classes.items():
        classes[key] = storage.count(key)
    return jsonify(classes)
