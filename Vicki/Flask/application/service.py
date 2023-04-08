# from application.models.employee import Employee
# from application.models.manager import Manager
# from application import db

from application.models.album import Album
from application.models.artist import Artist
from application.models.customer import Customer
from application.models.genre import Genre
from application.models.loan_procedure import LoanProcedure
from application.models.record_label import RecordLabel
from application import db



def get_all_customers():
    return db.session.query(Customer).all()

def get_customer_by_id(cust_id):
    if cust_id > 0:
        return db.session.query(Customer).filter_by(cust_id=cust_id).first()
    else:
        return None


def get_album_by_id(album_id):
    if album_id < 100:
        album = db.session.query(Album).filter_by(album_id=album_id).first()
        return album
    else:
        return None


def save_new_customer(cust):
    db.session.add(cust)
    db.session.commit()


def get_artist_by_id(art_id):
    if art_id < 100:
        artist = db.session.query(Artist).filter_by(art_id=art_id).first()
        return artist
    else:
        return None
