#!/bin/usr/env python

from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.login import LoginManager
from app import config

# construct a db object for our entire application
db = SQLAlchemy()
csrf = CsrfProtect()
lm = LoginManager()


def load_models():
    from app.users import models

load_models()


def init_extentions(app):
    db.init_app(app)
    csrf.init_app(app)
    lm.init_app(app)


def init_views(app):
    from app.views import home
    from app.users.views import BP as userBP

    app.register_blueprint(userBP)
    app.register_blueprint(home)

    lm.login_view = 'login'


def create_app(config=config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.debug = True

    init_extentions(app)
    init_views(app)

    return app

manager = Manager(create_app)
