import psycopg2
from psycopg2.errors import DuplicateDatabase, DuplicateTable
from psycopg2 import OperationalError

data = {
    'user': 'postgres', #postgres
    'password': 'coderslab2',
    'port': '5432',
    'host': 'localhost', #localhost
    'dbname': 'postgres'
}


def connect (connection_data = None):
    if connection_data is None:
        connection_data = data
    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True
    return connection





def create_db(dbname):
    sql = f"""
    CREATE DATABASE {dbname};
    """

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        print("Database has been established")
        conn.close()
    except DuplicateDatabase as err:
        print("This database name is already in use", err)
    except OperationalError as oerr:
        print("You have no connection with database", oerr)


create_db("japa")

query1 = """
CREATE TABLE Users(
id serial,
PRIMARY KEY(id),
name varchar(60),
email varchar(60) UNIQUE,
password varchar(60)
)
"""

query2 = """
CREATE TABLE Messages(
id serial PRIMARY KEY,
user_id int REFERENCES Users(id),
message text
)
"""

query3 = """
CREATE TABLE Items(
id serial PRIMARY KEY,
name varchar(40),
description text,
price decimal (7,2)
)
"""

query4 = """
CREATE TABLE Orders(
id serial,
PRIMARY KEY(id),
description text
)
"""

query5 = """
CREATE TABLE ItemsOrders(
id serial PRIMARY KEY,
item_id int REFERENCE Items(id) ON DELETE CASCADE,
order_id int REFERENCE Orders(id) ON DELETE CASCADE
)
"""
query6 = """
SELECT * FROM Items WHERE price > 13
"""

query7 = """
INSERT INTO Orders(description) VALUES ('przykładowy opis')
"""

query8 = """
DELETE FROM Users WHERE id = 7
"""
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
query9 = """
SELECT Users.name AS user_name, Users.id AS user_id, Messages.messages AS u_message
FROM Users JOIN Messages ON Users.id=Messages.user_id
"""
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
query10 = """
ALTER TABLE Messages ADD date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
"""




#zad 3

def dividers(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


for item in dividers(18):
    print(item)
