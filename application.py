#!/usr/bin/env python

# from flask import request
# from flask import Flask, session, jsonify
# from flask import render_template, redirect
# from flask import url_for
# import json
# from datetime import datetime as dt
# app = Flask(__name__)

# @app.route('/home/')
# def hello():
# 	return "hellowwwwwe"

# @app.route('/')
# def index():
# 	generate_img("c1-1.jpeg"); #save inside static folder
# 	return '<img src=' + url_for('media/scanned_chunks/ch/',filename='c1-1.jpeg') + '>' 

# if __name__ == "__main__":
# 	app.run()


from flask import Flask, redirect, url_for

app = Flask(__name__)
# @app.route('/')
# def index():
# 	# generate_img("test.jpeg") #save inside static folder
# 	return '<img src=' + url_for('static/cn',filename='c1_0001.png') + '>'

@app.route('/<lang>/<id>')
def index(lang,id):
	# generate_img("test.jpeg") #save inside static folder
	fn=lang+'c1_'+id+'.png'
	return '<img src=' + url_for('static',filename=fn) + '>'


if __name__ == "__main__":
	app.run(debug=True)