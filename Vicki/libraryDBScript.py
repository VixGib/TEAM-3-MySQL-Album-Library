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

# ask which customer information to see using first name
# name = input("Which customer would you like? ")
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name, email, mobile_num, join_date FROM customer WHERE first_name = :param"),
#         {"param": name}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  \nLast Name: {row.last_name} \nemail: {row.email} \nMobile Num: {row.mobile_num} \nJoin Date: {row.join_date}")


# #print('************* join *********')
# fname = input("What is the customer's first name? ")
# lname = input("What is the customer's last name? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select c.first_name cust_first_name, c.last_name cust_last_name, c.cust_id, l.loan_album_id , l.due_back_date
#         from customer c inner join loan_procedure l
#         on c.cust_id = l.loan_cust_id where c.first_name = :fname and c.last_name = :lname"""),
#         {"fname": fname, "lname" : lname}
#     )
#     for row in result:
#         print(f"First Name: {row.cust_first_name}  \nLast Name: {row.cust_last_name} \nCustomer Id: {row.cust_id} \nAlbum Id: {row.loan_album_id} \nDue Back Date: row.{row.due_back_date}")


# with engine.connect() as conn:
#     result = conn.execute(
#         text("""update manager set first_name = 'Christmas' where man_id = 3""")
#     )
#     conn.commit()




