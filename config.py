import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    CSRF_ENABLED = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_TLS = 1
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'
    ADMINS = ['admin@gmail.com']
    POSTS_PER_PAGE = 3
    ELASTICSEARCH_URL ='http://localhost: 9200'


SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
CSRF_ENABLED = True

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
# MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
MAIL_USE_TLS = 1
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
POSTS_PER_PAGE = 3
ELASTICSEARCH_URL='http://localhost:9200'
