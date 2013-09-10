#!/bin/usr/env python

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    # fields are always of the db.Column class
    id = db.Column(db.Integer, primate_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    # this is to tell how to print these objects
    def __repr__(self):
        return '<User %r>' % (self.nickname)
