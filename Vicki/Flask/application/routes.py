from flask import render_template, jsonify, request
from application.models.album import Album
from application.models.artist import Artist
from application.models.customer import Customer
from application.models.genre import Genre
from application.models.loan_procedure import LoanProcedure
from application.models.record_label import RecordLabel
from application import db

from application import app, service

# ALL CUSTOMERS
@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    return render_template('customer.html', customers=customers, message=error, title="All Customer's Information")
    # return jsonify(customers)


# CUSTOMERS BY ID
# this is a ReST endpoint - only returns data
@app.route('/customers/<int:cust_id>', methods=['GET'])
def show_customer(cust_id):
    error = ""
    customer = service.get_customer_by_id(cust_id)
    if not customer:
        return jsonify("There is no customer with ID: " + str(cust_id))
    else:
        print(customer.first_name, customer.last_name)
    # return jsonify(customer)
    return render_template('customerIndividual.html', customer=customer, cust_id=cust_id, message=error, title="Customer Information")


# ALL ALBUMS
@app.route('/albums', methods=['GET'])
def show_albums():
    error = ""
    albums = service.get_all_albums()
    if len(albums) == 0:
        error = "There are no albums to display"
    return render_template('allAlbum.html', albums=albums, message=error, title="All Albums")
    #return jsonify(albums)


# ALBUMS BY ID
@app.route('/album/<int:album_id>', methods=['GET'])
def get_album(album_id):
    error = ""
    album = service.get_album_by_id(album_id)
    if not album:
        error = "There is no album with ID: " + str(album_id)
    return render_template('albumIndividual.html', album=album, album_id=album_id, message=error, title="Album by ID")
    # return jsonify(album)


# ALL ARTISTS
@app.route('/artists', methods=['GET'])
def show_artists():
    error = ""
    artists = service.get_all_artists()
    if len(artists) == 0:
        error = "There are no artist's to display"
    return render_template('allArtists.html', artists=artists, message=error, title="All Artists")
    # return jsonify(artists)


# ARTIST BY ID AND SHOW ALBUMS
@app.route('/artists/<int:art_id>', methods=['GET'])
def get_artist(art_id):
    error = ""
    artist = service.get_artist_by_id(art_id)
    if not artist:
        error = "There is no artist with ID: " + str(art_id)
    return render_template('artist.html', artist=artist, art_id=art_id, message=error, title="Artists and Albums")
    # return jsonify(artist)


# ALL LOANS
@app.route('/loans', methods=['GET'])
def show_loans():
    error = ""
    loans = service.get_all_loans()
    if len(loans) == 0:
        error = "There are no loans to display"
    return render_template('allLoans.html', loans=loans, customer=Customer, loan_cust_id=Customer.cust_id, message=error, title="All loans")
    # return jsonify(loans)


# CREATE NEW CUSTOMER
@app.route('/customers', methods=['POST'])
def create_customer():
    # data is a dictionary
    data = request.get_json()
    # need to create an object of type Manager with the data
    cust = Customer(first_name=data['first_name'], last_name=data['last_name'],email=data['email'], mobile_num=data['mobile_num'], address=data['address'], postcode=data['postcode'], join_date=data['join_date'])
    print(cust)
    service.save_new_customer(cust)
    return jsonify(cust)


# GET ALL CUSTOMER LOAN ALBUMS BY LAST NAME
@app.route('/customers/<last_name>', methods=['GET'])
def get_customer_by_last_name(last_name):
    error = ""
    album_names =[]
    count = 0
    customer = service.get_customer_by_last_name(last_name)
    if not customer:
        error = "There is no customer with surname: " + str(last_name)
    else:
        for l in customer.loans:
            album = service.get_album_by_id(l.loan_album_id)
            album_names.append(album.album_name)
            count += 1
    return render_template('customer_loan_history.html', album_names=album_names, customer=customer, last_name=last_name, message=error)
    # return jsonify(customer)

# SEARCH GENRE BY NAME AND RETURN ALL ALBUMS
@app.route('/genres/<genre_name>', methods=['GET'])
def get_genre(genre_name):
    error = ""
    artist_first_names = []
    artist_last_names = []
    genre = service.get_genre_by_genre_name(genre_name)
    if not genre:
        error = "There is noe genre with this name:" + str(genre_name)
    else:
        for a in genre.albumsG:
            artist = service.get_artist_by_id(a.artist_id)
            artist_first_names.append(artist.first_name)
            artist_last_names.append(artist.last_name)

    return render_template('genre.html', genre=genre, genre_name=genre_name, artist_first_names=artist_first_names, artist_last_names=artist_last_names, message=error, title="Albums by Genre")
    # return jsonify(genre)




