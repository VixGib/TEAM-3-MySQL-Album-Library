from application import db
from dataclasses import dataclass

# # ORM - Object relational mapping - mapping class to a table
# # DTO - data transfer object


@dataclass
class LoanProcedure(db.Model):

    loan_id: int
    loan_album_id: int
    loan_cust_id: int
    issue_date: str
    due_back_date: str

    loan_id = db.Column(db.Integer, primary_key=True, nullable=False)
    loan_album_id = db.Column(db.Integer, db.ForeignKey('album.album_id'), nullable=False)
    loan_cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id'), nullable=False)
    issue_date = db.Column(db.Date)
    due_back_date = db.Column(db.Date)

