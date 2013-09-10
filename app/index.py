#!/usr/bin/env python

from flask import Flask, render_template

import datetime
import servo
import RPIO

from crontab import CronTab

RPIO.setup(25, RPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
			'title' : 'HELLO! WORLD!',
			'time': timeString
			}
	return render_template('main.html', **templateData)

@app.route("/feed/<howMuch>")
def feedAmount(howMuch):
	howMuch = int(howMuch)
	if howMuch > 5:
		howMuch = 5
	try:
		servo.servo_CW(howMuch)
		servo.servo_CCW(howMuch)
		response = "NOM NOM NOM"
	except:
		response = "Could not feed, still hungry"

	templateData = {
			'title' : 'Feeding time',
			}
	return render_template('feed.html', **templateData)

@app.route("/feed")
def feed():
	try:
		servo.servo_CW(howMuch)
		response = "NOM NOM NOM"
	except:
		response = "Could not feed, still hungry"

	templateData = {
			'title' : 'Feeding time',
			}
	return render_template('feed.html', **templateData)

@app.route("/led/<action>")
def light(action):
	if action == "on":
		RPIO.output(25, True)
	if action == "off":
		RPIO.output(25, False)
	
	tData = {
		'action': action
		}
#	print "turning led " + tData.action
	return render_template('led.html', **tData)

@app.route("/cron")
def set_cron():
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)

