from flask import Flask, request
from connection import connect

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = """
             <form method='POST'>
                 Product name:<input type='text' name='name'>
                 <br>Description:<input type='text' name='description'>
                 <br>Price: <input type='float' name='price'>
                 <br><input type='submit' value='Submit'>"""
    if request.method == 'GET':
        return form
    elif request.method == 'POST':

        #try:
        price = float(request.form['price'])
        #except ...

        if len(request.form['name']) <= 40 and 0 < price <= 99999.99:
            sql = f"""
            INSERT INTO items(name, description, price) VALUES ('{request.form['name']}', '{request.form['description']}', '{request.form['price']}')
            """

            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql)

            return form + "Product added!"
        else:
            return form + "Invalid data!"



if __name__ == '__main__':
    app.run(debug=True)
