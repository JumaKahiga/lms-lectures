import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.views.index import HelloWorld, LoadData
from config import config_settings

environment = os.getenv('ENVIRONMENT')

db = SQLAlchemy()
migrate = Migrate()


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

    return app
