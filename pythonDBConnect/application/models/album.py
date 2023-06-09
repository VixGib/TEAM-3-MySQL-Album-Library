from application import db
from dataclasses import dataclass
@dataclass
# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Album(db.Model):
    album_id = db.Column(db.Integer, primary_key=True, nullable=False)
    album_name = db.Column(db.String(150), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.art_id'), nullable=False)
    album_genre_id= db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable = False)
    record_label_id = db.Column(db.Integer, db.ForeignKey('record_label.rec_id'), nullable=True)
    album_year = db.Column(db.Date)
