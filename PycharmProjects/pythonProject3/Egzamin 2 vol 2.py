import psycopg2
import psycopg2.errors
from connection import connect

sql = """
CREATE DATABASE db_exam
"""

def db_create():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
    except psycopg2.errors.DuplicateDatabase as err:
        return err
    except psycopg2.OperationalError as err:
        return err


print(db_create())

query1 = """
CREATE TABLE Users(
id serial PRIMARY KEY,
name varchar(60),
email varchar(60),
password varchar(60)
)
"""

query2 = """
CREATE TABLE Messages(
id serial PRIMARY KEY,
user_id int REFERENCES Users.id,
message text
)
"""

query3 = """
CREATE TABLE Items(
id serial PRIMARY KEY,
name varchar(40),
description text,
price decimal(7,2)
)
"""

query4 = """
CREATE TABLE Orders(
id serial PRIMARY KEY,
description text
)
"""

query5 = """
CREATE TABLE ItemsOrders(
id serial PRIMARY KEY,
item_id int REFERENCES Item(id),
order_id int REFERENCES Order(id)
)
"""

query6 = """
SELECT * FROM Item WHERE price > 13
"""

query7 = """
INSERT INTO Orders(description) VALUES ('przykladowy opis')
"""

query8 = """
DELETE FROM User WHERE id = 7
"""

query9 = """
SELECT User.name FROM User
INNER JOIN Messages
ON User.id = Messages.user_id
"""

query10 = """
ALTER TABLE Messages ADD date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""

def dividers(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

for i in dividers(6):
    print(i)



from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/add_product', methods = ['GET', 'POST'])
def add_product():
    HTML = """
            <form method='POST'>
                Product name: <input name='name' type=text><br>
                Description: <input name='description' type=text><br>
                Price: <input name='price' type=float>
                <input type=submit> 
            </form>
            """
    if request.method == 'GET':
        return HTML
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        try:
            price = float(request.form.get('price'))
        except Exception as err:
            return HTML + err
        if len(name) <= 40 and 0 < price < 99999.99:
            conn = connect()
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO Items(name, description, price) VALUES ('{name}', '{description}', '{price}')
            """
            cursor.execute(sql)
            return HTML + "Product added"
        else:
            return HTML + "Invalid data"



if __name__ == '__main__':
    app.run()
