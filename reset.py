from sqlalchemy import create_engine

import secret
from app import db, app


def reset_database():
    url = 'mysql+pymysql://root:{}@localhost/?charset=utf8mb4'.format(
        secret.database_password
    )
    e = create_engine(url, echo=True)

    with e.connect() as connection:
        connection.execute('DROP DATABASE IF EXISTS blog')
        connection.execute('CREATE DATABASE blog CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        connection.execute('USE {}'.format(secret.database_schema_name))

    # db.metadata.create_all(bind=e)


if __name__ == '__main__':
    with app.app_context():
        reset_database()
