#!/bin/usr/env python

from wtforms import Form

# class to create cron job forms
class CronForm(Form):
	name = TextField(name, validators=[DataRequired()])

