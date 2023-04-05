from sqlalchemy import create_engine
from sqlalchemy import text

# using root user is not a great idea!!
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'Library'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    #mysql+pymysql://root:@127.0.0.1:3306/Company
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))


engine = get_connection()
# selected all the first and last names from the customer table
# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT * FROM customer"))
#         for row in result:
#             print(f"First Name: {row.first_name}  Last Name: {row.last_name}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)

# select Album name and year from album table
# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT album_name, album_year FROM album"))
#         for row in result:
#             print(f"Album Name: {row.album_name} Album Year: {row.album_year}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)

# print('******parameterised query ********')
# ask which customer information to see using the customer id

# num = int(input("Which customer would you like? "))
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name FROM customer WHERE cust_id = :param"),
#         {"param": num}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  Last Name: {row.last_name}")

#Look up all American Artists
# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT first_name, last_name FROM artist WHERE nationality = 'American'"))
#         for row in result:
#             print(f"First Name: {row.first_name} Last Name: {row.last_name}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)

#look up album before 1980
# try:
#     with engine.connect() as conn:
#         result = conn.execute(
#             text("""SELECT a.album_name alb_name, b.first_name art_first_name, b.last_name art_last_name
#                                    FROM album a inner join artist b
#                                    on a.artist_id = b.art_id WHERE album_year < 1980 """))
#         for row in result:
#             print(f"Album Name: {row.alb_name} Last Name: {row.art_first_name} Last Name: {row.art_last_name}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)


# Add a new customer

# with engine.connect() as conn:
#     result = conn.execute(
#     text("""insert into customer (cust_id, first_name, last_name, email, mobile_num, address, postcode, join_date)
#     values (18,'Joan', 'Walker', 'joanwalker@email.com', '07951465874', '25 Green Row', 'WA16 5TR', '2023-01-04')"""),
#          )
#
#     conn.commit()

# ask which customer information to see using first name
# name = input("Which customer would you like? ")
# with engine.connect() as conn:
#     result = conn.execute(
#        text("SELECT first_name, last_name, email, mobile_num, join_date FROM customer WHERE first_name = :param"),
#         {"param": name}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  \nLast Name: {row.last_name} \nemail: {row.email} \nMobile Num: {row.mobile_num} \nJoin Date: {row.join_date}")


#print('************* join *********')

#using customer first name and last name bring up loan information
# fname = input("What is the customer's first name? ")
# lname = input("What is the customer's last name? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""SELECT c.first_name cust_first_name, c.last_name cust_last_name, c.cust_id, l.loan_album_id, l.due_back_date
#         from customer c inner join loan_procedure l
#         on c.cust_id = l.loan_cust_id where c.first_name = :fname and c.last_name = :lname"""),
#         {"fname": fname, "lname" : lname}
#     )
#     for row in result:
#         print(f"First Name: {row.cust_first_name}  \nLast Name: {row.cust_last_name} \nCustomer Id: {row.cust_id} \nAlbum Id: {row.loan_album_id} \nDue Back Date: {row.due_back_date}")

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

 # query for member search for a chosen album
# cust_first = input("What is your first name? ")
# cust_last = input("What is your last name? ")
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
#         print(f"""Loan ref: {row.loan_id} \nIssue date: {row.issue_date} \nCustomer Name: {row.cust_first_name} {row.cust_last_name} \nAlbum: {row.album_name}""")

# NOT WORKING TRYING TO ADD ARTIST, RECORD LABEL AND ALBUM IN 1
# with engine.connect() as conn:
#     result = conn.execute(
#     text("""insert into artist (first_name, last_name, nationality)
#     values ('Jessie', 'J', 'English' )
#     insert into record_label (rec_id, label_name)
#     values (20, 'Lava Music and Universal Republic')
#     insert into album(album_name, artist_id, album_genre_id, record_label_id, album_year)
#     values ('Alive', 15, 1, 20, '2013')"""),
#          )
#
#     conn.commit()

#search artist details
# name = input("What is the artist's first name? ")
#
# with engine.connect() as conn:
#      result = conn.execute(
#          text("""select if(first_name=last_name, first_name, concat(first_name," ",last_name)) as artistName, nationality
#          from artist where first_name = :param"""),
#          {"param": name}
#      )
#
# for row in result:
#     print(f"Artist Name: {row.artistName}  \nNationality: {row.nationality} \n")


# search artist details by initial
# initial = input("What is the artist's first initial? ")
#
# with engine.connect() as conn:
#      result = conn.execute(
#          text("""select if(first_name=last_name, first_name, concat(first_name," ",last_name)) as artistName, nationality
#          from artist where first_name like concat(:param, '%')"""),
#          {"param": initial}
#      )
#
# for row in result:
#     print(f"Artist Name: {row.artistName}      Nationality: {row.nationality}")


# search all artists of one nationality
# nat = input("What nationality would you like to browse? ")
#
# with engine.connect() as conn:
#      result = conn.execute(
#          text("""select if(first_name=last_name, first_name, concat(first_name," ",last_name)) as artistName, nationality
#          from artist where nationality = :param"""),
#          {"param": nat}
#      )
# print(f"Here is a list of {nat} artists:")
# for row in result:
#     print(f"{row.artistName}")

# browse by label (join)
# label = input("What record label would you like to browse? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select a.album_name, r.label_name
#          from album a inner join record_label r on a.record_label_id=r.rec_id where r.label_name = :param"""),
#         {"param": label}
#     )
# print(f"Here is a list of albums on the {label} label:")
# for row in result:
#     print(f"{row.album_name}")

# insert a new album
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""insert into album (album_name, artist_id, album_genre_id, record_label_id, album_year) values ("Nobody Else", 8, 1, 7, 1995)""")
#     )
#     conn.commit()

# Add a new customer

with engine.connect() as conn:
    result = conn.execute(
    text("""insert into customer (first_name, last_name, email, mobile_num, address, postcode, join_date)
    values ('Andrew', 'Walker', 'andrewwalker@email.com', '07973846621', '25 Lime Grove', 'WA6 7TR', '2023-01-04')""")
         )

    conn.commit()

# with engine.connect() as conn:
#     result = conn.execute(
#         text("""update manager set first_name = 'Christmas' where man_id = 3""")
#     )
#     conn.commit()