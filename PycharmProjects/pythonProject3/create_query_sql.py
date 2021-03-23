# bedzie na egz
author_query = """
CREATE TABLE author(
    id serial,
    first_name varchar(20),
    last_name varchar(20),
PRIMARY KEY (id)
)
"""

book_query = """
CREATE TABLE book(
    id serial,
    title varchar(30),
    id_author integer,
PRIMARY KEY (id),
FOREIGN KEY(id_author) REFERENCES author(id)
)
"""

creation_query_list = [author_query, book_query]