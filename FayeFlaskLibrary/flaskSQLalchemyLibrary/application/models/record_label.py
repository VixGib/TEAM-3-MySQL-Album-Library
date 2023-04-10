from application import db
from dataclasses import dataclass

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
@dataclass
class Record_label(db.Model):
    rec_id: int
    label_name: str

    rec_id = db.Column(db.Integer, primary_key=True, nullable=False)
    label_name = db.Column(db.String(70), nullable=False)
    albumsR = db.relationship('Album', backref='albumsR')