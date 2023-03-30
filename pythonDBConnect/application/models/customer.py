from application import db
from dataclasses import dataclass

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Customer(db.Model):
    cust_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    email= db.Column(db.String, nullable = False)
    mobile_num = db.Column(db.String(11), nullable=True)
    address=db.Column(db.String(150), nullable=True)
    postcode = db.Column(db.String(8), nullable=True)
    join_date = db.Column(db.Date)
    loans = db.relationship('Loan_procedure', backref='loans')

