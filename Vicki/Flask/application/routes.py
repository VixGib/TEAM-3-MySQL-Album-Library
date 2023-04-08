from flask import render_template, jsonify, request
from application.models.album import Album
from application.models.artist import Artist
from application.models.customer import Customer
from application.models.genre import Genre
from application.models.loan_procedure import LoanProcedure
from application.models.record_label import RecordLabel
from application import db

from application import app, service


@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no customers to display"
    return render_template('customer.html', customers=customers, message=error)
    # return jsonify(customers)


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
    return render_template('customerIndividual.html', customer=customer, cust_id=cust_id, message=error)


@app.route('/album/<int:album_id>', methods=['GET'])
def get_album(album_id):
    error = ""
    album = service.get_album_by_id(album_id)
    if not album:
        error = "There is no album with ID: " + str(album_id)
    return render_template('albumIndividual.html', album=album, album_id=album_id, message=error, title=album.album_name)
    # return jsonify(album)

@app.route('/customers', methods=['POST'])
def create_customer():
    # data is a dictionary
    data = request.get_json()
    # need to create an object of type Manager with the data
    cust = Customer(first_name=data['first_name'], last_name=data['last_name'],email=data['email'], mobile_num=data['mobile_num'], address=data['address'], postcode=data['postcode'], join_date=data['join_date'])
    print(cust)
    service.save_new_customer(cust)
    return jsonify(cust)


@app.route('/artists/<int:art_id>', methods=['GET'])
def get_artist(art_id):
    error = ""
    artist = service.get_artist_by_id(art_id)
    if not artist:
        error = "There is no artist with ID: " + str(art_id)
    return render_template('artist.html', artist=artist, art_id=art_id, message=error, title="Artists and Albums")
    # return jsonify(artist)

