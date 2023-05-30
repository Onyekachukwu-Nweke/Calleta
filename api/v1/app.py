#! usr/bin/python3
"""API For Calleta App"""
from flask import Flask, request, jsonify, make_response, abort, render_template
from os import environ
from api.v1.views import app_views
from models import storage
from flask_cors import CORS
# from flasgger import Swagger
# from flasgger.utils import swag_from


app = Flask(__name__)

cors = CORS(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """closes database on teardown"""
    storage.close()

@app.errorhandler(404)
def notfound(msg):
    """handles 404 errors"""
    return make_response(jsonify({'err 404': 'not found'}), 404)

if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)