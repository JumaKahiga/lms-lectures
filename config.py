import os


class Config:
    DEBUG = True
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG = False


config_settings = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
        }
