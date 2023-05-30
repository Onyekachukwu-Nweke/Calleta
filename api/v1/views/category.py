#! usr/bin/python3
from models import storage
from models.category import Category
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify


@app_views.route('/categories', method=['GET'], strict_slashes=False)
def get_categories():
    """
    Retrieves all the categories from db
    """
    all_categories = storage.all(Category).values()
    list_categories = []
    for category in all_categories:
        list_categories.append(category.to_dict())
    return make_response(jsonify(list_categories), 200)
