#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""initializes a new route"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": "amenities",
           "City": "cities",
           "Place": "places",
           "Review": "reviews",
           "State": "states",
           "User": "users"}

classes = {"Amenity": "amenities",
           "City": "cities",
           "Place": "places",
           "Review": "reviews",
           "State": "states",
           "User": "users"}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})


@app_views.route('/stats',  methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of each objects by type"""
    objs = {"aneminities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    return jsonify(objs)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns a JSON: number of each objects by type"""
    stats = {}
    for key, value in classes.items():
        stats[value] = storage.count(key)
    return jsonify(stats)
