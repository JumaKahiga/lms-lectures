from flask import make_response, jsonify
from flask_restful import Resource
from sqlalchemy.sql import func

from app.models.lectures_model import Lecture


class RandomLecture(Resource):
    def get(self):
        try:
            random_lecture = Lecture.query.order_by(func.random()).first()
        except Exception:
            return make_response(jsonify(
                {'error': 'No lectures found'}))
        lecture_dict = random_lecture.toJson()

        if not lecture_dict:
            return make_response(jsonify(
                {'error': 'No lectures found'}))

        return make_response(jsonify(
            {'lecture': lecture_dict}), 200)
