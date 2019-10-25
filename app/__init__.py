import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from app.models import db
from app.views.index import HelloWorld, LoadData
from app.views.register import CreateUser, CreateAdmin
from config import config_settings

migrate = Migrate()

environment = os.getenv('ENVIRONMENT')


def create_app(config=environment):
    app = Flask(__name__)
    app.config.from_object(config_settings[environment])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    api = Api(app)
    api.add_resource(HelloWorld, '/')
    api.add_resource(LoadData, '/load_data')
    api.add_resource(CreateUser, '/user/register')
    api.add_resource(CreateAdmin, '/admin/register')

    return app
