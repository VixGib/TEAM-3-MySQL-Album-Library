from application import db
from dataclasses import dataclass


#
# # ORM - Object relational mapping - mapping class to a table
# # DTO - data transfer object
@dataclass
class Artist(db.Model):
    art_id: int
    first_name: str
    last_name: str
    nationality: str

    art_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    nationality = db.Column(db.String(70))
    albumsA = db.relationship('Album', backref='albumsA')
