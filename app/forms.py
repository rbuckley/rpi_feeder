#!/bin/usr/env python

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

# class to create cron job forms
class CronForm(Form):
	name = TextField('name', validators=[DataRequired()])

