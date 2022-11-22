
from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__,
                static_url_path='',
                static_folder='web/static',
                template_folder='web/templates')

    app.secret_key = 'some_secret'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .todo.todo_app import todo_app as todo_blueprint
    app.register_blueprint(todo_blueprint)

    return app
