#!/bin/usr/env pythong
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'  os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'dp_repo')

CSRF_ENABLED = True
SECRET_KEY = 'kjlashj298lkn)(&21l'
