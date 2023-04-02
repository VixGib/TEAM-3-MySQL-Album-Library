from application import db
from dataclasses import dataclass
#
# # the annotation below will help to turn the Python object into a JSON object
# @dataclass
# class Manager(db.Model):
#
#     man_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     employees = db.relationship('Employee', backref='employees')

class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    genre_name = db.Column(db.String, nullable=False)
    albumsG = db.relationship('Album', backref='albumsG')
