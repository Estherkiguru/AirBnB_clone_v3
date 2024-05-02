#!/usr/bin/python3
"""
create a route on the object app_views
Returns: status 'OK'
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    """
    Returns states: 'OK'
    """
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route("/stats")
def get_stats():
    """
    Retrieves the number of each objects by type
    """
    stats = {
            "amenites": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
    }
    return jsonify(stats)
