from application import db
from dataclasses import dataclass


#
# # ORM - Object relational mapping - mapping class to a table
# # DTO - data transfer object
@dataclass
class RecordLabel(db.Model):
    rec_id: int
    label_name: str

    rec_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    label_name = db.Column(db.String(70), nullable=False)
    albumsR = db.relationship('Album', backref='albumsR')
