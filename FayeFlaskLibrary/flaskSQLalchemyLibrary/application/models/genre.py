from application import db
from dataclasses import dataclass

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object

@dataclass
class Genre(db.Model):

    genre_id: int
    genre_name: str

    genre_id = db.Column(db.Integer, primary_key=True, nullable=False)
    genre_name = db.Column(db.String(70), nullable=False)
    albumsG = db.relationship('Album', backref='albumsG')