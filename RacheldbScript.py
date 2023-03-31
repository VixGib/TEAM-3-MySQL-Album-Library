from sqlalchemy import create_engine
from sqlalchemy import text

# using root user is not a great idea!!
user = 'root'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'Library'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    # mysql+pymysql://root:@127.0.0.1:3306/Company
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))

engine = get_connection()

# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT * FROM manager"))
#         for row in result:
#          print(f"First Name: {row.first_name}  Last Name: {row.last_name}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)
#
# print('******parameterised query ********')

# num = int(input("What manager would you like? "))
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name FROM manager WHERE man_id = :param"),
#         {"param": num}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  Last Name: {row.last_name}")
#
# name = input("What manager would you like? ")
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name FROM manager WHERE first_name = :param"),
#         {"param": name}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  Last Name: {row.last_name}")

# browse query by artist
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select if(first_name = last_name, last_name, concat(first_name, " ", last_name)) as artist, album_name as album
# from artist join album on art_id = artist_id order by artist;"""),
#         )
#     print("{:25s}  {:s}".format("Artist:", "Album:"))
#     for row in result:
#         print(f"{row.artist:25s}  {row.album:s} ")
#     print("")
#
# # browse query by genre
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select genre_name as genre, if(first_name = last_name, last_name, concat(first_name, " ", last_name)) as artist, album_name as album
# from artist join album on art_id = artist_id join genre on genre_id = album_genre_id order by genre;"""),
#         )
#     print("{:15s}  {:25s}  {:s}".format("Genre:", "Artist:", "Album:"))
#     for row in result:
#         print(f"{row.genre:15s}  {row.artist:25s}  {row.album:s} ")
#     print("")
#
# # query for member search for a chosen album
# a_name = input("What album would you like? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select album_id, genre_name,
#         if(first_name = last_name, last_name, concat(first_name, " ", last_name)) as artist,
#         album_name, album_year from artist join album on art_id = artist_id join genre on genre_id = album_genre_id
#         where album_name = :a_name"""),
#         {"a_name": a_name}
#     )
#
#     for row in result:
#         print(f"""Album id: {row.album_id} Genre: {row.genre_name} Artist Name: {row.artist} Album Name: {row.album_name} Year: {row.album_year}""")
#
# # query for member search for a chosen album
# cust_first = input("What is your first name? ")
# cust_last  = input("What is your last name? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select loan_id, issue_date, customer.first_name as cust_first_name, customer.last_name as cust_last_name, album_name
# from loan_procedure left outer join customer on loan_cust_id = cust_id
# join album on album_id = loan_album_id
# where customer.first_name = :cust_first and customer.last_name = :cust_last"""),
#         {"cust_first": cust_first, "cust_last": cust_last}
#     )
#
#     for row in result:
#         print(f"""Loan ref: {row.loan_id} Issue date: {row.issue_date}
#         Customer Name: {row.cust_first_name} {row.cust_last_name} Album: {row.album_name}""")

# basic insert test
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""insert into loan_procedure(loan_id, issue_date, due_back_date, loan_cust_id, loan_album_id)
#         values (99, "2023-03-31", "2023-04-21", 2, 7)"""),
#         )
#     conn.commit()

# customer borrow
# cust_name = input("What is your full name? ")
# a_name = input("What album do you wish to loan? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""insert into loan_procedure(issue_date, due_back_date, loan_cust_id, loan_album_id)
#         values (curdate(), (curdate() + interval 3 week),
#         (select cust_id from customer where concat(customer.first_name, " ", customer.last_name) = :cust_name limit 1),
#         (select album_id from album where album_name = :a_name limit 1) )"""),
#             {"a_name": a_name, "cust_name": cust_name}
#         )
#     conn.commit()

# popular albums
with engine.connect() as conn:
    result = conn.execute(
        text("""select distinct album_name as album, count(loan_album_id) as no_loans 
from loan_procedure join album on album_id = loan_album_id group by album_name order by count(loan_album_id) desc"""),
        )
    print("{:30s}  {:s}".format("Album:", "Number of loans:"))
    for row in result:
        print(f"{row.album:30s}  {row.no_loans:d} ")
    print("")

# with engine.connect() as conn:
#     result = conn.execute(
#         text("""update manager set first_name = 'Christmas' where man_id = 3""")
#     )
#     conn.commit()