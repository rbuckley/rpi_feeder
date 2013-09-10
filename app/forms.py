#!/bin/usr/env python

from wtforms import Form
from wtforms import TextField
from wtforms.validators import Required

# class to create cron job forms
class CronForm(Form):
	name = TextField(name, validators=[DataRequired()])

