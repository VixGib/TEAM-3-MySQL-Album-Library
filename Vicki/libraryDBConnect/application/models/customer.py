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

@dataclass
class Customer(db.Model):
    cust_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(70), nullable=False)
    mobile_num = db.Column(db.String(11), nullable=False)
    address = db.Column(db.String(150), nullable=True)
    postcode = db.Column(db.String(8), nullable=True)
    join_date = db.Column(db.Date, nullable=True)
    loans = db.relationship('Loan_procedure', backref='loans')
