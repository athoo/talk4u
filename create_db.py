#!/usr/bin/env python

from flask import request
from flask import Flask, session, jsonify
from flask import render_template, redirect

import json
from datetime import datetime as dt

from models import db, Book
# /Users/cscnthu/david_file/talk4u/db

app = Flask('application')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/cscnthu/david_file/talk4u/db/test.db'
db.init_app(app)
app.run()
db.create_all()
db.session.commit()

# 'sqlite://///home/cly/Documents/py_practice_code/database/database.db'
if __name__=='__main__':

	user_condition = Book(book_id="1", name="trials",author="saddas",publisher="sdasds",read_length=100,category="sdlashdkash")
	print user_condition
	# print db
	db.session.add(user_condition)
	db.session.commit()