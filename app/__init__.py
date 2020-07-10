from flask import Flask
from flask_migrate import Migrate

from app.errors import register_error
from app.models import db, login
from config import Config
import logging
from logging.handlers import SMTPHandler
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)
mail = Mail(app)




def register_blueprints():
    from app.views import app as views
    app.register_blueprint(views)


def main():
    register_blueprints()
    register_error(app)
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
