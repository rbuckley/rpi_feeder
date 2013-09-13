#!/bin/usr/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from app import config

# construct a db object for our entire application
db = SQLAlchemy()

def load_models():
    from app.users import models

load_models()

def init_extentions(app):
    db.init_app(app)


def init_views(app):
    from app import views
    
    app.register_blueprint(views.home)

def create_app(config=config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extentions(app)
    init_views(app)

    return app

manager = Manager(create_app)
