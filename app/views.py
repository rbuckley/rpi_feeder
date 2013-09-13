#!/usr/bin/env python

from flask import Flask, render_template, Blueprint


import datetime

home = Blueprint('home', __name__, template_folder='templates')

@home.route("/index")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
			'title' : 'HELLO! WORLD!',
			'time': timeString
			}
	return render_template('main.html', **templateData)

