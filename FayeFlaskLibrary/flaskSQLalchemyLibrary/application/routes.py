from flask import render_template, jsonify, request
from application.models.customer import Customer
from application.models.album import Album
from application.models.artist import Artist
from application.models.record_label import Record_label
from application.models.genre import Genre
from application.models.loan_procedure import Loan_procedure

from application import app, service

# shows all customers
@app.route('/customers', methods=['GET'])
def show_customers():
    error = ""
    customers = service.get_all_customers()
    if len(customers) == 0:
        error = "There are no employees to display"
    return render_template('customer.html', customers=customers, message=error)
    # return jsonify(customers)

# this is a ReST endpoint - only returns data
# shows only 1 customer
@app.route('/customers/<int:cust_id>', methods=['GET'])
def show_customer(cust_id):
    error = ""
    customer = service.get_customer_by_id(cust_id)
    if not customer:
        return jsonify("There is no employee with ID: " + str(cust_id))
    else:
        print(customer.first_name, customer.last_name)
    # return jsonify(customer)
    return render_template('customerIndividual.html', customer=customer, cust_id=cust_id, message=error)

# shows the details of just one album
@app.route('/album/<int:album_id>', methods=['GET'])
def get_album(album_id):
    error = ""
    album = service.get_album_by_id(album_id)
    if not album:
        error = "There is no album with ID: " + str(album_id)
    return render_template('albumIndividual.html', album=album, message=error, album_id=album_id, title=album.album_name)
    # return jsonify(album)

# adds a customer to the customer table, used postman
@app.route('/customers', methods=['POST'])
def create_customer():
    # data is a dictionary
    data = request.get_json()
    # need to create an object of type Manager with the data
    cust = Customer(first_name = data['first_name'],last_name = data['last_name'], email = data['email'], mobile_num=data['mobile_num'], address=data['address'], postcode=data['postcode'], join_date=data['join_date'] )
    print(cust)
    service.save_new_customer(cust)
    return jsonify(cust)

# gets artist by id and in html lists that artists albums
@app.route('/artists/<int:art_id>', methods=['GET'])
def get_artist(art_id):
    error = ""
    artist = service.get_artist_by_id(art_id)
    if not artist:
        error = "There is no artist with ID: " + str(art_id)
    return render_template('artist.html', artist=artist, message=error, title="Artists and Albums")
    # return jsonify(artist)


# @app.route('/customers/<last_name>', methods=['GET'])
# def get_customer_by_last_name(last_name):
#     error = ""
#     customer = service.get_customer_by_last_name(last_name)
#     if not customer:
#         error = "There is no customer with surname: " + str(last_name)
#     else:
#         for l in customer.loans:
#             album=service.get_album_by_id(l.loan_album_id)
#     return render_template('customer_loan_history.html', album=album, customer=customer, last_name=last_name, message=error)
#     # return jsonify(customer)


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