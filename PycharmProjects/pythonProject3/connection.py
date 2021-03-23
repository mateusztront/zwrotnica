import psycopg2

data = {
    'user': 'postgres',
    'password': 'coderslab',
    'port': '5432',
    'host': 'localhost',
    'dbname': 'nowa_baza'
}


def connect (connection_data = None):
    if connection_data is None:
        connection_data = data
    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True
    return connection

if __name__ == '__main__': # działa tylko jezeli odpali sie w tym pliku, przy imporcie funkcji connect to sie nie wykona
    connection = connect()
    connection.close()