from flask import make_response, jsonify, request
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}