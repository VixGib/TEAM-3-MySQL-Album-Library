from application import db
from dataclasses import dataclass
#
# # the annotation below will help to turn the Python object into a JSON object
@dataclass
# class Manager(db.Model):
#
#     man_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     employees = db.relationship('Employee', backref='employees')


class Artist(db.Model):
    art_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    nationality = db.Column(db.String(70))
    albumsA = db.relationship('Album', backref='albumsA')
