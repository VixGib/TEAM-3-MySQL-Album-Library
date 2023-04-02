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

class Loan_procedure(db.Model):
    loan_id = db.Column(db.Integer, primary_key=True, nullable=False)
    loan_album_id = db.Column(db.Integer, db.ForeignKey('album.album_id'), nullable=False)
    loan_cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id'), nullable=False)
    issue_date = db.Column(db.Date)
    due_back_date = db.Column(db.Date)

