from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

from .views.index import HelloWorld


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(HelloWorld, '/')

    return app
