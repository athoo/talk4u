#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import request
from flask import Flask, session, jsonify
from flask import render_template, redirect,url_for

import json
from datetime import datetime as dt
from models import db, Book, Category, Chapter, Chunk, Audio

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/cscnthu/david_file/talk4u/db/test.db'
db.init_app(app)

templist = []

@app.route('/')
def hello():
	return 'the server is now working'

@app.route('/books/')
def listbooks():
	response = ""
	for item in Book.query.all():
		response += ('\n'+item.name)

	return response

@app.route('/books/<book_id>')
def listonebook(book_id):
	book = Book.query.filter_by(isbn = book_id ).first()
	response = {}
	response['name'] = book.name
	response['isbn'] = book.isbn
	response['author'] = book.author
	response['read_length'] = book.read_length
	response['publisher'] = book.publisher
	return jsonify(response)

@app.route('/books/<book_id>/chapters')
def listchapters(book_id):
	book = Book.query.filter_by(isbn = book_id ).first()
	for item in Chapter.query.filter_by(book_id = book.id).all():
		templist.append(item.num)
	return str(templist)

@app.route('/books/<book_id>/audio/')
def listaudios(book_id):
	book = Book.query.filter_by(isbn = book_id ).first()
	chapter = Chapter.query.filter_by(book_id = book.id).first()
	for chunk in Chunk.query.filter_by(chapter_id = chapter.id).all():
		audio = Audio.query.filter_by(chunk_id = chunk.id).first()
		templist.append(audio.audiopiece_link)
	return str(templist)

@app.route('/books/<book_id>/chapters/<chapter_id>/chunks/')
def listchunksofonechapter(book_id,chapter_id):
	book = Book.query.filter_by(isbn = book_id ).first()
	chapter = Chapter.query.filter_by(book_id = book.id).first()
	for chunk in Chunk.query.filter_by(chapter_id = chapter.id).all():
		templist.append(chunk.chunk_text_link)
	return str(templist)


# /books/<book-id>/chapters/<chapter-id>/audio/
# all audio files (highest rated) of the chapter
@app.route('/books/<book_id>/chapters/<chapter_id>/audio/')
def listallaudioofchapter(book_id,chapter_id):
	book = Book.query.filter_by(isbn = book_id ).first()
	chapter = Chapter.query.filter_by(book_id = book.id).first()
	for chunk in Chunk.query.filter_by(chapter_id = chapter.id).all():
		audio = Audio.query.filter_by(chunk_id = chunk.id).first()
		templist.append(audio.audiopiece_link)
	return str(templist)	

@app.route('/chunks/<chunk_id>')
def listonechunk(chunk_id):
	chunk = Chunk.query.filter_by(id = chunk_id).first()
	return '<img src=' + url_for('static',filename = chunk.chunk_text_link) + '>'

@app.route('/chunks/<chunk_id>/audio/')
def listaudiosofonechunk(chunk_id):
	chunk = Chunk.query.filter_by(id = chunk_id).first()
	for audio in Audio.query.filter_by(chunk_id = chunk.id).all():		templist.append(audio.audiopiece_link)
	return str(templist)

@app.route('/audio/<audio_id>')
def listoneaudio(audio_id):
	audio = Audio.query.filter_by(id = audio_id).first()
	return str(audio.audiopiece_link)

#not finish for the rating
@app.route('/audio/<audio_id>/rating')
def listratingofaudio(audio_id):
	audio = Audio.query.filter_by(id = audio_id).first()
	return str(audio.rating)
# /audio/<audio-id>/rating/
# represent rating of the audio file
# rating range from 1 to 5


if __name__ == "__main__":
	app.run(debug=True)
