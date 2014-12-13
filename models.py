#!/usr/bin/env python

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    book_id = db.Column(db.String(10),primary_key=True, unique=True)
    name = db.Column(db.String(160))
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    read_length = db.Column(db.Integer)
    category = db.Column(db.String(80))

    def __init__(self,book_id,name,author,publisher,read_length):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.publisher = publisher
        self.read_length = read_length
        self.category = category

# collect all the category and combine them together for fast index
class Category(db.Model):


# share the same id to link two element together
class Chunk(db.Model):
    uuid = db.Column(db.String(40), primary_key=True, unique=True)
    trials = db.Column(db.String(80))

    def __init__(self, uuid, trials):
        self.uuid = uuid
        self.trials = ','.join(trials)

    def __repr__(self):
        return '<User_cond %s> %s' % (self.uuid, self.trials)

class AudioPiece(db.Model):
    def __init__(self,):



# 
class Chapter(db.Model):
    def __init__(self,):
