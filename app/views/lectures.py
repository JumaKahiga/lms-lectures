from flask import make_response, jsonify
from flask_restful import Resource

from app.models.lectures_model import Lecture


class FetchAllLectures(Resource):
    def get(self, start_page, items_per_page):
        try:
            start_page = int(start_page)
            items_per_page = int(items_per_page)
        except ValueError:
            return make_response(jsonify(
                {'error': 'only integers allowed for page numbers'}), 400)

        print(type(start_page))

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
