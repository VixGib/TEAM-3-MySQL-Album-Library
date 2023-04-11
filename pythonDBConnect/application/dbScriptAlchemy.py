from application import db

from application.models.album import Album
from application.models.artist import Artist
from application.models.customer import Customer
from application.models.genre import Genre
from application.models.loan_procedure import Loan_procedure
from application.models.record_label import Record_label

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
user = 'root'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'Library'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))

engine = get_connection()
Session = sessionmaker(bind=engine)

session = Session()

# Martina's code...
# manager = session.query(Manager).filter_by(first_name="Santa").first()
# print(manager.first_name, manager.last_name, manager.man_id, manager.employees)
# for e in manager.employees:
#     print(e.first_name, end = " ")
#     print(e.last_name)

# customer = session.query(Customer).filter_by(first_name="Bobby").first()
# print(customer.first_name, customer.last_name, customer.cust_id)
# for e in customer.loans:
#     album = session.query(Album).filter_by(album_id=e.loan_album_id).first()
#     print(album.album_name)
#     print("Issue date: ", e.issue_date, end = " ")
#     print("Due back date: ", e.due_back_date)
#
# genre = session.query(Genre).filter_by(genre_name="Pop").first()
# print(len(genre.albumsG), genre.genre_name, "albums:")
# for e in genre.albumsG:
#     print(e.album_name, ": ", e.album_year)

#
# genre = session.query(Genre).filter_by(genre_name="Pop").first()
# print("There are", len(genre.albumsG), genre.genre_name, "albums:")
# for e in genre.albumsG:
#     print(e.album_name, ": ", e.album_year)
#     artist = session.query(Artist).filter_by(art_id=e.artist_id).first()
#     if artist.first_name == artist.last_name:
#         print("Artist:", artist.first_name,'\n')
#     else:
#         print("Artist:", artist.first_name, artist.last_name,'\n')


# genre object
# genre = Genre(genre_name="Opera")
# session.add(genre)
# session.commit()

# # customer object
# customer = Customer(first_name="David", last_name="Beckham", email="davidbeckham@email.com", mobile_num="07898654234", address="3 Mansion Lane", postcode="CA3 1DD", join_date="2014-06-07")
# session.add(customer)
# session.commit()

# DELETE A GENRE BY ID
# session.query(Genre).filter_by(genre_id=16).delete()
# session.commit()