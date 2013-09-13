#!/usr/bin/env python
from flask import request, render_template, flash, g, sessions, redirect, url_for

from app.users import bp
from app.users.models import User
from app.users.forms import RegisterForm, LoginForm
from app.users.decorators import requires_login

@bp.route("/me/")
@requires_login
def home():
    return render_template("profile.html", user=g.user)

@bp.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id']  = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('users.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("login.html", form=form)

@bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data))
        dp.session.add(user)
        dp.session.commit()

        session['user_id'] = user.id

        flash('Thanks for registering')
        return redirect(url_for('users.home'))
    return render_template("register.html", form=form)
  

