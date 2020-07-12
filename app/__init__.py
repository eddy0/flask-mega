from elasticsearch import Elasticsearch
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment

import secret
from app.errors import register_error
from app.models import db, login
from config import Config
import logging
from logging.handlers import SMTPHandler
from flask_mail import Mail

app = Flask(__name__)

app.config.from_object(Config)
uri = 'mysql+pymysql://root:{}@localhost/{}?charset=utf8mb4'.format(
    secret.database_password,
    secret.database_schema_name
)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']])

# socketio = SocketIO(app)
#
#
# @socketio.on('event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))
#     global count
#     count += 1
#     emit('response', {'message': '{0} has joined'.format(count)})


def register_blueprints():
    from app.views import app as views
    app.register_blueprint(views, url_prefix='/')
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


def main():
    register_blueprints()
    register_error(app)
    # socketio.run(app, host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
