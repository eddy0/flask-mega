from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate

from app.models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)


def main():
    from app.views import app as views
    app.register_blueprint(views)
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
