from connection import  connect



def select_data(tablica):
    selector = f"""
    SELECT * FROM {tablica}
    """

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(selector)
    data = cursor.fetchall()
    conn.close()
    return data
if __name__ == "__main__":
    select_data()

