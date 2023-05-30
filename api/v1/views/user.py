#! usr/bin/python3
from models import storage
from models.user import User
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify


@app_views.route('/register', method=['GET', 'POST'], strict_slashes=False)
def register():
    """Register a user/shopper"""
    content = request.get_json(silent=True)
    if type(content) is not dict:
        return make_response(jsonify("Not a JSON"), 400)
    fname = content.get('firstname')
    lname = content.get('lastname')
    email = content.get('email')
    phone = content.get('phone')
    password = content.get('password')

@app_views.route('/login', method=['POST'], strict_slashes=False)
def login():
    """Logs a user/shopper into the application"""
    login_details = request.get_json(silent=True)
    if type(login_details) is not dict:
        return make_response(jsonify("Not a JSON"), 400)
    email = login_details.get("email")
    password = login_details.get("password")

    if email:
        