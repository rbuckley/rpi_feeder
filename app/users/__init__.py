#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint("users", __name__, template_folder="templates", url_prefix='/users')

from app.users import views

