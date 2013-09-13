#!/bin/usr/env python

from app import db
from app.users import constants as USER

class User(db.Model):
    __tablename__ = 'users'
    # fields are always of the db.Column class
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default = USER.USER)
    status = db.Column(db.SmallInteger, default = USER.NEW)


    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    # this is to tell how to print these objects
    def __repr__(self):
        return '<User %r>' % (self.nickname)

user_group = db.Table("user_group", db.Column("user_id", db.Integer, db.ForeignKey(User.id), primary_key=True))
