#! usr/bin/python3
from models import storage
from models.product import Product
from api.v1.views import app_views
from flask import abort, make_response, request, redirect, jsonify


@app_views.route('/products', method=['GET'], strict_slashes=False)
def get_all_products():
    """
    Retrieves the list of all product objects
    or a specific user
    """
    all_products = storage.all(Product).values()
    list_products = []
    for prdt in all_products:
        list_products.append(prdt.to_dict())
    return make_response(jsonify(list_products), 200)

@app_views.route('/products/<product_id>', method=['GET'], strict_slashes=False)
def view_product(product_id):
    """
    Retrieves a particular product from
    db using the product id
    """
    product = storage.get(Product, product_id)
    if not product:
        abort(404)
    return make_response(jsonify(product.to_dict()), 200)
