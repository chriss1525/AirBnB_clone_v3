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
