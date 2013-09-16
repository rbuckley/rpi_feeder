#!/usr/bin/env python
from functools import wraps

from flask import g, flash, redirect, url_for


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(u'You need to be logged in for this page.')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function
