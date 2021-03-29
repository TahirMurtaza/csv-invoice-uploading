import os
basedir = os.path.abspath(os.path.dirname(__file__))


from os.path import join, dirname, realpath


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'asd5d5asd56ad6asd8679wqw64wq8486g4h'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/csv_data"
    UPLOAD_EXTENSIONS = ['.csv']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_SETTINGS= 'config.DevelopmentConfig'
    UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/')

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True