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
#         result = conn.execute(text("SELECT first_name, last_name FROM customer"))
#         for row in result:
#          print(f"First Name: {row.first_name}  Last Name: {row.last_name}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)

# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT album_name, album_year FROM album"))
#         for row in result:
#          print(f"Album: {row.album_name}  Year of release: {row.album_year}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)

print('******parameterised query ********')

# num = int(input("What customer would you like? "))
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name FROM customer WHERE cust_id = :param"),
#         {"param": num}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  Last Name: {row.last_name}")
#
# name = input("What customer would you like? ")
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name, email, mobile_num, join_date FROM customer WHERE first_name = :param"),
#         {"param": name}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  Last Name: {row.last_name} \nEmail: {row.email} \nTel no: {row.mobile_num} \nJoin date: {row.join_date}\n")


# print('************* join *********')
# fname = input("What is the customer's first name? ")
# lname = input("What is the customer's last name? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select c.first_name cust_fname, c.last_name cust_lname, c.cust_id, l.loan_album_id, l.due_back_date
#         from customer c inner join loan_procedure l
#         on c.cust_id= l.loan_cust_id where c.first_name = :fname and c.last_name= :lname"""),
#         {"fname": fname, "lname" : lname}
#     )
#     for row in result:
#         print(f"First Name: {row.cust_fname}  Last Name: {row.cust_lname} Customer Id: {row.cust_id} Loan: {row.loan_album_id} Due back: {row.due_back_date}")
#

# with engine.connect() as conn:
#     result = conn.execute(
#         text("""update customer set last_name = 'Brooks' where cust_id = 3""")
#     )
#     conn.commit()


# search artist details
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
with engine.connect() as conn:
    result = conn.execute(
        text("""insert into album (album_name, artist_id, album_genre_id, record_label_id, album_year) values ("Nobody Else", 8, 1, 7, 1995)""")
    )
    conn.commit()