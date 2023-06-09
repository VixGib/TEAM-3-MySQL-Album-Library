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


class Record_label(db.Model):
    rec_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    label_name = db.Column(db.String(70), nullable=False)
    albumsR = db.relationship('Album', backref='albumsR')
