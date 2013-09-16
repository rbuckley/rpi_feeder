#!/usr/bin/env python
from flask import request, render_template, flash, g, session
from flask import redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users import BP
from app.users.models import User
from app.users.forms import RegisterForm, LoginForm
from app.users.decorators import requires_login


@BP.route("/me/")
@requires_login
def home():
    """Render the users home page"""
    return render_template("users/profile.html", user=g.user)


@BP.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@BP.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('users.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("users/login.html", form=form)


@BP.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data,
                    password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        flash('Thanks for registering')
        return redirect(url_for('users.home'))
    print "hello woooorld"
    return render_template("users/register2.html", form=form)
