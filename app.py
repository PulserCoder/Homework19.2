from flask import Flask
from flask_restx import Api
from dao.model.user import User
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns
from views.auth import auth_ns

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)

def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True
create_data(app, db)
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=3000, debug=True)
