#! usr/bin/python3
from models import storage
from models.category import Category
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

