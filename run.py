#!/usr/bin/env python

from app import create_app

test = create_app()
test.debug = True

test.run(host='0.0.0.0')
