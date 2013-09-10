#!/usr/bin/env python

from RPIO import PWM

import time

# todo: find out which pin controls the servo
ServoPin = 17

# servo variable
servo = PWM.Servo()

def servo_CW(sleep_time):
	# rotate the servo clockwise
	servo.set_servo(ServoPin, 1200)
#	time.sleep(sleep_time)
	servo.stop_servo(ServoPin)
	time.sleep(0.25)

def servo_CCW(sleep_time):
	# rotate the servo counter-clockwise
	servo.set_servo(ServoPin, 2000)
#	time.sleep(sleep_time)
	servo.stop_servo(ServoPin)
	time.sleep(0.25)
