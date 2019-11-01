from flask import make_response, jsonify
from flask_restful import Resource

from app.models.lectures_model import Lecture, Review
from app.models.person_model import User
from app.utilities.validators import validate_string


class FetchAllLectures(Resource):
    def get(self, start_page, items_per_page):
        try:
            start_page = int(start_page)
            items_per_page = int(items_per_page)
        except ValueError:
            return make_response(jsonify(
                {'error': 'only integers allowed for page numbers'}), 400)

        if not start_page:
            start_page = 1

        if not items_per_page:
            items_per_page = 20

        lectures = Lecture.query.paginate(
            start_page, items_per_page, False)

        data = []

        for lecture in lectures.items:
            data.append(lecture.toJson())

        return make_response(jsonify(
            {
                'lectures': data,
                'total_lectures': lectures.total,
                'current_page': lectures.page,
                'next_page': lectures.next_num
                }), 200)


class FetchTopTenLectures(Resource):
    def get(self):
        data = []
        results = Review.highest_rated_lectures()

        if not results:
            return make_response(jsonify(
                {'error': 'No lectures found'}), 404)

        for result in results:
            lecture = Lecture.query.get(result).toJson()
            data.append(lecture)

        return make_response(jsonify(
            {'lectures_count': len(data), 'lectures': data}), 200)


class FilterLectures(Resource):
    def get(self, author_name):
        if author_name and not validate_string(author_name):
            return make_response(jsonify(
                {'error': 'author name must be a string'}))

        author_name.capitalize()

        user = User.query.filter(User.name.contains(author_name)).first()

        data = []

        if not user:
            return make_response(jsonify(
                {
                    'message': f'no lecture found with {author_name} as author'
                }), 200)

        for lecture in user.lectures:
            data.append(lecture.toJson())

        return make_response(jsonify(
            {
                'lectures': data,
                'total_lectures': len(data),
                }), 200)
