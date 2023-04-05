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
password = ''
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
# MARTINA'S CODE
# manager = session.query(Manager).filter_by(first_name="Santa").first()
# print(manager.first_name, manager.last_name, manager.man_id, manager.employees)
# for e in manager.employees:
#     print(e.first_name, end = " ")
#     print(e.last_name)


# # SEARCH FOR ALBUM NAME AND LOAN AND DATES BY CUSTOMER FIRST NAME
# customer = session.query(Customer).filter_by(first_name="Vicki").first()
# print("Customer Name:", customer.first_name, customer.last_name, "\nLoan id:", customer.cust_id)
# for e in customer.loans:
#     print("Issue Date: ", e.issue_date)
#     print("Due Back Date: ", e.due_back_date)
#     album = session.query(Album).filter_by(album_id=e.loan_album_id).first()
#     print("Album due bask:",album.album_name)


## SEARCH GENRE FOR ALL POP ALBUMS AND RETURN ALBUM NAME AND YEAR
# genre = session.query(Genre).filter_by(genre_name="Pop").first()
# print(len(genre.albumsG), genre.genre_name, "Albums")
# for e in genre.albumsG:
#     print(e.album_name,":", e.album_year)


## SEARCH ARTIST BY ARTIST FIRST NAME AND PRINT ALL ALBUMS FOR THAT ARTIST
# artist = session.query(Artist).filter_by(first_name="pink").first()
# if artist.first_name == artist.last_name:
#     print("Here are the albums by", artist.first_name,":")
# else:
#     ("Here are the albums by", artist.first_name, artist.last_name, ":")
# for e in artist.albumsA:
#     print(e.album_name)

# # SEARCH FOR ALL ALBUMS BY ONE ARTIST USING FIRST NAME
# artists = session.query(Artist).filter_by(first_name="George").all()
# print("The albums by", artists[0].first_name, artists[0].last_name, "are:")
# for e in artists[0].albumsA:
#     print(e.album_name)

# #SEARCH FOR ALL ALBUMS FROM A PARTICULAR YEAR
# albums = session.query(Album).filter_by(album_year="1995").all()
# print("The albums from", albums[0].album_year, "are:")
# for e in albums:
#     print(e.album_name)


## SEARCH GENRE FOR ALL POP ALBUMS AND RETURN HOW MANY ALBUMS, THE ALBUM NAME, YEAR AND ARTIST NAME
# genre = session.query(Genre).filter_by(genre_name="Pop").first()
# print("There are", len(genre.albumsG), genre.genre_name, "Albums")
# for e in genre.albumsG:
#     print(e.album_name,":", e.album_year)
#     artist = session.query(Artist).filter_by(art_id=e.artist_id).first()
#     if artist.first_name == artist.last_name:
#         print("Artist:", artist.first_name, "\n")
#     else:
#         print("Artist:", artist.first_name, artist.last_name, "\n")


# USER STORY 1 SEARCH FOR ALL ALBUMS BY AMERICAN ARTISTS
# artists = session.query(Artist).filter_by(nationality="American").all()
# print("There are", len(artists), artists[0].nationality, "Artists")
# for e in artists:
#     if e.first_name == e.last_name:
#         print("\nArtist:", e.first_name)
#     else:
#         print("\nArtist:", e.first_name, e.last_name)
#     album = session.query(Album).filter_by(artist_id=e.art_id).all()
#     for a in album:
#         print("Album:", a.album_name)


## MARTINA'S CODE
# # manager object
# manager = Manager(first_name="Man1", last_name="Man2")
# # inserting it into the database
# session.add(manager)
# # don't forget to commit!
# session.commit()


## ADD ANOTHER GENRE
# genre = Genre(genre_name="Opera")
# session.add(genre)
# session.commit()


## ADD A NEW CUSTOMER
# customer = Customer(first_name="David", last_name="Beckham", email="davidbeckham@email.com", mobile_num="07658395584", address="43 Football Road", postcode="LL2 5GT", join_date="2023-04-01")
# session.add(customer)
# session.commit()


## DELETE A GENRE BY ID
# session.query(Genre).filter_by(genre_id=16).delete()
# session.commit()