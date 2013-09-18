#!/usr/bin/env python
from functools import wraps

from flask import g, flash, redirect, url_for


def requires_login(func):
    """ decorator to check login on a route """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ the actual function for checking """
        if g.user is None:
            flash(u'You need to be logged in for this page.')
            return redirect(url_for('users.login'))
        return func(*args, **kwargs)
    return decorated_function
