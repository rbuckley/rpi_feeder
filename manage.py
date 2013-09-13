#!/usr/bin/env python

from app import manager

@manager.command
def myrun():
    manager.runserver("0.0.0.0", debug = True)

manager.run()
