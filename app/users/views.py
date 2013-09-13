#!/usr/bin/env python

from app.users import bp
from app.users.models import User

@bp.route("/<username>")
def hello(username):
    return "Hello, " + username
