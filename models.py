#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/cscnthu/david_file/talk4u/db/test.db'
db = SQLAlchemy(app)
# db = SQLAlchemy()

# association_table = Table('association', Base.metadata,
#     Column('left_id', Integer, ForeignKey('left.id')),
#     Column('right_id', Integer, ForeignKey('right.id'))
# )
# collect all the category and combine them together for fast index
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True, unique=True)
    name = db.Column(db.String(40))

    def __init__(self,name):
        self.name = name

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True, unique=True)
    name = db.Column(db.String(160))
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    read_length = db.Column(db.Integer)
    isbn = db.Column(db.String(20))

    # category = db.Column(db.String(80))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('books', lazy='dynamic'))

    def __init__(self,name,author,publisher,read_length,isbn,category):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.read_length = read_length
        self.isbn = isbn
        self.category = category

# get the chapter list, bit by bit to get the name
class Chapter(db.Model):
    id = db.Column(db.Integer,primary_key=True, unique=True)
    num = db.Column(db.Integer)
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'))
    book = db.relationship('Book',backref=db.backref('chapters',lazy='dynamic'))

    def __init__(self,num,book):
        self.num = num
        self.book = book

# share the same id to link two element together
class Chunk(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    chunk_text_link = db.Column(db.String(100))
    chapter_id = db.Column(db.Integer,db.ForeignKey('chapter.id'))
    chapter = db.relationship('Chapter',backref=db.backref('chunks',lazy='dynamic'))

    def __init__(self,chunk_text_link,chapter):
        self.chunk_text_link = chunk_text_link
        self.chapter = chapter

class Audio(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    audiopiece_link = db.Column(db.String(60))

    chunk_id = db.Column(db.Integer,db.ForeignKey('chunk.id'))
    chunk = db.relationship('Chunk',backref=db.backref('audios',lazy="dynamic"))

    def __init__(self,audiopiece_link,chunk):
        self.audiopiece_link = audiopiece_link
        self.chunk = chunk

