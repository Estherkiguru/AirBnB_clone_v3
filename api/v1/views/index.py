#!/usr/bin/python3
"""
create a route on the object app_views
Returns: status 'OK'
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def api_status():
    """
    Returns states: 'OK'
    """
    status = {"status": "OK"}
    return jsonify(status)
