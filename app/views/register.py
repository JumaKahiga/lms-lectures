import json
from flask import make_response, jsonify
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app.models.person_model import Admin, User
from app.utilities.validators import (
    validate_email, validate_string)


class CreateUser(Resource):
    def __init__(self):
        self._parser = RequestParser()
        self._parser.add_argument('name', type=str)
        self._parser.add_argument(
            'email', type=str, required=True, help='email is required')
        self._parser.add_argument(
            'password', required=True, help='password cannot be blank')
        self._parser.add_argument('bio', type=str)
        self._parser.add_argument('company', type=str)
        self._parser.add_argument('avatar_url', type=str)
        self._parser.add_argument('social_urls', type=list)

    def post(self):
        data = self._parser.parse_args()
        email = data.get('email')

        user_obj = User()

        if not validate_email(email):
            return make_response(jsonify(
                {'error': 'invalid email'}), 400)

        for key, value in data.items():
            if key in ('name', 'password', 'bio') and not validate_string(value):
                return make_response(jsonify(
                    {'error': f'invalid characters used for {key}'}), 400)
            else:
                setattr(user_obj, key, value)
        user = User.query.filter_by(email=email).scalar()

        if user:
            return make_response(jsonify(
                {'error': f'a user with the email {email} already exists'}), 400)

        user_obj.password_hash = user_obj.set_password(user_obj.password)
        new_user = user_obj.save()
        new_user = json.dumps(new_user, default=str)

        return make_response(
            jsonify(
                {
                    'message': 'User registered successfully',
                    'data': new_user
                }
                ), 201)


class CreateAdmin(Resource):
    def __init__(self):
        self._parser = RequestParser()
        self._parser.add_argument(
            'name', type=str, required=True, help='name is required')
        self._parser.add_argument(
            'email', type=str, required=True, help='email is required')
        self._parser.add_argument(
            'password', required=True, help='password cannot be blank')

    def post(self):
        data = self._parser.parse_args()
        email = data.get('email')

        admin_obj = Admin()

        if not validate_email(email):
            return make_response(jsonify(
                {'error': 'invalid email'}), 400)

        for key, value in data.items():
            if key in ('name',) and not validate_string(value):
                return make_response(jsonify(
                    {'error': f'invalid characters used for {key}'}), 400)
            else:
                setattr(admin_obj, key, value)
        admin = Admin.query.filter_by(email=email).scalar()

        if admin:
            return make_response(jsonify(
                {'error': f'an admin with the email {email} already exists'}), 400)

        admin_obj.password_hash = admin_obj.set_password(admin_obj.password)
        new_admin = admin_obj.save()
        new_admin = json.dumps(new_admin, default=str)

        return make_response(
            jsonify(
                {
                    'message': 'Admin registered successfully',
                    'data': new_admin
                }
                ), 201)
