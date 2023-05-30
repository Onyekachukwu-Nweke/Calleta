#! usr/bin/python3
from models import storage
from models.user import User
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify


@app_views.route('/register', method=['GET', 'POST'], strict_slashes=False)
def register():
    """Register a user/shopper"""
    content = request.get_json(silent=True)
