from application import db
from dataclasses import dataclass



# # ORM - Object relational mapping - mapping class to a table
# # DTO - data transfer object
@dataclass
class Album(db.Model):

    album_id: int
    album_name: str
    artist_id: int
    album_genre_id: int
    record_label_id: int
    album_year: str

    album_id = db.Column(db.Integer, primary_key=True, nullable=False)
    album_name = db.Column(db.String(150), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.art_id'), nullable=False)
    album_genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable=False)
    record_label_id = db.Column(db.Integer, db.ForeignKey('record_label.rec_id'), nullable=True)
    album_year = db.Column(db.String, nullable=True)
    albumloan = db.relationship('LoanProcedure', backref='albumloan')
