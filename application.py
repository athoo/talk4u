#!/usr/bin/env python

from flask import request
from flask import Flask, session, jsonify
from flask import render_template, redirect

import json
from datetime import datetime as dt

app = Flask(__name__)
app.cinfig['SQLALCHEMY_DATABASE_URI'] ='sqlite:////db/chunks.db' 