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

    #check if a user exists
    user_exists = storage.get_user(email, User)
    if user_exists:
        return make_response(jsonify("User Exists"), 400)
    if request.method == 'POST':
        new_user = User(**content)
        new_user.save()
        response = jsonify(new_user.to_dict())
        response.status_code = 201
        return response

@app_views.route('/login', method=['POST'], strict_slashes=False)
def login():
    """Logs a user/shopper into the application"""
    login_details = request.get_json(silent=True)
    if type(login_details) is not dict:
        return make_response(jsonify("Not a JSON"), 400)
    email = login_details.get("email")
    password = login_details.get("password")

    if email:
        user = storage.get(email, User)
        if not user:
            return make_response(jsonify("User does not exist"), 400)
        if password != user.password:
            return make_response(jsonify("Wrong password, Try Again"), 400)
