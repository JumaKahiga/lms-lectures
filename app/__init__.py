import os
from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from app.models import db
from app.views.index import RandomLecture
from app.views.login import LoginAdmin, LoginUser
from app.views.register import CreateUser, CreateAdmin
from app.views.seed_data import LoadData
from config import config_settings

migrate = Migrate()

environment = os.getenv('ENVIRONMENT')
secret_key = os.getenv('SECRET_KEY')


def create_app(config=environment):
    app = Flask(__name__)
    app.config.from_object(config_settings[environment])
    app.config['JWT_SECRET_KEY'] = secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    jwt = JWTManager(app)
    CORS(app)
    api = Api(app)
    api.add_resource(RandomLecture, '/')
    api.add_resource(LoadData, '/load_data')
    api.add_resource(CreateUser, '/user/register')
    api.add_resource(CreateAdmin, '/admin/register')
    api.add_resource(LoginAdmin, '/admin/login')
    api.add_resource(LoginUser, '/user/login')

    return app
