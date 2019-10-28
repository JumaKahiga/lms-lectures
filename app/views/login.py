from flask import make_response, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token)
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app.models.person_model import Admin, User
from app.utilities.validators import (
    validate_email, validate_string)


class LoginAdmin(Resource):
    def __init__(self):
        self._parser = RequestParser()
        self._parser.add_argument(
            'email', type=str, required=True, help='email cannot be blank')
        self._parser.add_argument(
            'password', required=True, help='invalid password')

    def post(self):
        data = self._parser.parse_args()
        email = data.get('email')
        password = data.get('password')

        if not validate_email(email):
            return make_response(jsonify(
                {'error': 'invalid email'}), 400)

        if not validate_string(password):
            return make_response(jsonify(
                {'error': 'invalid password'}), 400)

        admin_obj = Admin.query.filter_by(email=email).first()

        if not admin_obj:
            return make_response(jsonify(
                {'error': f'user with the email {email} does not exist'}), 404)

        validated = admin_obj.authenticate_password(password)

        if not validated:
            return make_response(jsonify(
                {'error': 'password and email did not match'}), 400)

        access_dict = {
                        'access_token': create_access_token(
                            identity={
                                        'email': email,
                                        'is_admin': True,
                                        'id': admin_obj.id
                            }, fresh=True),
                        'refresh_token': create_refresh_token(
                            identity={
                                        'email': email,
                                        'is_admin': True,
                                        'id': admin_obj.id
                            })
                        }

        return make_response(jsonify(
            {'message': 'login successful', 'tokens': access_dict}), 200)


class LoginUser(Resource):
    def __init__(self):
        self._parser = RequestParser()
        self._parser.add_argument(
            'email', type=str, required=True, help='email cannot be blank')
        self._parser.add_argument(
            'password', required=True, help='invalid password')

    def post(self):
        data = self._parser.parse_args()
        email = data.get('email')
        password = data.get('password')

        if not validate_email(email):
            return make_response(jsonify(
                {'error': 'invalid email'}), 400)

        if not validate_string(password):
            return make_response(jsonify(
                {'error': 'invalid password'}), 400)

        user_obj = User.query.filter_by(email=email).first()

        if not user_obj:
            return make_response(jsonify(
                {'error': f'user with the email {email} does not exist'}), 404)

        validated = user_obj.authenticate_password(password)

        if not validated:
            return make_response(jsonify(
                {'error': 'password and email did not match'}), 400)

        access_dict = {
                        'access_token': create_access_token(
                            identity={
                                        'email': email,
                                        'is_author': user_obj.is_author,
                                        'id': user_obj.id
                            }, fresh=True),
                        'refresh_token': create_refresh_token(
                            identity={
                                        'email': email,
                                        'is_author': user_obj.is_author,
                                        'id': user_obj.id
                            })
                        }

        return make_response(jsonify(
            {'message': 'login successful', 'tokens': access_dict}), 200)
