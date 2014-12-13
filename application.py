#!/usr/bin/env python

from flask import request
from flask import Flask, session, jsonify
from flask import render_template, redirect

import json
from datetime import datetime as dt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////db/chunks.db' 
# db.init_app(app)

@app.route('/home/')
def hello():
	return "hellowwwwwe"


if __name__ == "__main__":
	app.run()