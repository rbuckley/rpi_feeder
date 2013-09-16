#!/usr/bin/env python

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo, Email


class LoginForm(Form):
    email = TextField('Email Address', [Required(), Email()])
    password = PasswordField('Password', [Required()])


class RegisterForm(Form):
    name = TextField('Nickname', [Required()])
    email = TextField('Email Address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirmPW = PasswordField('Confirm Password',
                              [
                                  Required(),
                                  EqualTo('password', message=
                                          'Passwords must match')
                              ])
