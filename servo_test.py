#!/usr/bin/env python

from RPIO import PWM

import time

servo = PWM.Servo()

while True:
	print "Neutral"
	# 1.5 ms
#	servo.set_servo(17, 1500)
#	time.sleep(1)
	print "Max pulse"
	# 2 ms
	servo.set_servo(17, 2700)
	time.sleep(1)
	print "Min pulse"
	# 1 ms
	servo.set_servo(17, 700)
	time.sleep(1)

	servo.stop_servo(17)

	time.sleep(5)
