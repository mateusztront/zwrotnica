from flask import Flask, request, render_template

from Selecting_data import select_data
from insert_data_to_db import dodaj_autora, dodaj_ksiazke

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("base.html")

@app.route('/add_authors', methods=['GET', 'POST'])
def author():
    if request.method == 'POST':
        dodaj_autora(**request.form)
    autorzy = select_data('author')
    return render_template("author.html", authors = autorzy)

@app.route('/add_books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        dodaj_ksiazke(**request.form)
    autorzy = select_data('author')
    ksiazki = select_data('book')
    return render_template("book.html", books = ksiazki, authors = autorzy)

if __name__ == '__main__':
    app.run()