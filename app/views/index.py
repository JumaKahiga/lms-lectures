from flask import make_response, jsonify, request
from flask_restful import Resource

from app.utilities.data_loader import DataLoadContextManager


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class LoadData(Resource):
    def post(self):
        file = request.files['file']
        with DataLoadContextManager(file) as f:
            return make_response(
                jsonify({'message': f}), 201)
        return make_response(jsonify(
            {'message': 'an error occured during seeding'}), 400)
