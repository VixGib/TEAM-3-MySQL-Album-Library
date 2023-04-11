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


# ALL CUSTOMERS
def get_all_customers():
    return db.session.query(Customer).all()


# CUSTOMERS BY ID
def get_customer_by_id(cust_id):
    if cust_id > 0:
        return db.session.query(Customer).filter_by(cust_id=cust_id).first()
    else:
        return None


# ALL ALBUMS
def get_all_albums():
    return db.session.query(Album).all()


# ALBUMS BY ID
def get_album_by_id(album_id):
    if album_id < 100:
        album = db.session.query(Album).filter_by(album_id=album_id).first()
        return album
    else:
        return None


# ALL ARTISTS
def get_all_artists():
    return db.session.query(Artist).all()


# ARTIST BY ID AND SHOW ALBUMS
def get_artist_by_id(art_id):
    if art_id < 100:
        artist = db.session.query(Artist).filter_by(art_id=art_id).first()
        return artist
    else:
        return None


# ALL LOANS
def get_all_loans():
    return db.session.query(LoanProcedure).all()


# CREATE NEW CUSTOMER
def save_new_customer(cust):
    db.session.add(cust)
    db.session.commit()


# GET ALL CUSTOMER LOAN ALBUMS BY LAST NAME
def get_customer_by_last_name(last_name):
    if len(last_name) > 0:
        customer = db.session.query(Customer).filter_by(last_name=last_name).first()
        return customer
    else:
        return None


# SEARCH GENRE BY NAME AND RETURN ALL ALBUMS
def get_genre_by_genre_name(genre_name):
    if len(genre_name) > 0:
        genre = db.session.query(Genre).filter_by(genre_name=genre_name).first()
        return genre
    else:
        return None

