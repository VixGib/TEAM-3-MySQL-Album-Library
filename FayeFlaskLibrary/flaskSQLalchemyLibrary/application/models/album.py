import datetime

from application import db
from dataclasses import dataclass
@dataclass
# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Album(db.Model):
    # which attributes are included in the JSON that I'm sending back
    album_id: int
    album_name: str
    artist_id: int
    album_genre_id: int
    record_label_id : int
    album_year: datetime.date

    album_id = db.Column(db.Integer, primary_key=True, nullable=False)
    album_name = db.Column(db.String(150), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.art_id'), nullable=False)
    album_genre_id= db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable = False)
    record_label_id = db.Column(db.Integer, db.ForeignKey('record_label.rec_id'), nullable=True)
    album_year = db.Column(db.Date)
    albumloan = db.relationship('Loan_procedure', backref='albumloan')