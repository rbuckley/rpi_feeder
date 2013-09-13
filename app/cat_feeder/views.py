#!/usr/bin/env python

from flask import Flask, render_template

@app.route("/feed/<howMuch>")
def feedAmount(howMuch):
	howMuch = int(howMuch)
	if howMuch > 5:
		howMuch = 5
	try:
		#servo.servo_CW(howMuch)
		#servo.servo_CCW(howMuch)
		response = "NOM NOM NOM"
	except:
		response = "Could not feed, still hungry"

	templateData = {
			'title' : 'Feeding time',
			}
	return render_template('cat_feeder/feed.html', **templateData)

@app.route("/feed")
def feed():
	try:
		#servo.servo_CW(howMuch)
		response = "NOM NOM NOM"
	except:
		response = "Could not feed, still hungry"

	templateData = {
			'title' : 'Feeding time',
			}
	return render_template('cat_feeder/feed.html', **templateData)

@app.route("/cron", methods = ['GET', 'POST'])
def set_cron():
    form = CronForm()
    if form.validate_on_submit():
        flash('You are trying to name this cron job"' + form.name.data + '"')
        return redirect('/index')
    return render_template('cat_feeder/cron.html', form = form)

