import sqlite3

connection = sqlite3.connect('brotheres.db')
cursor = connection.cursor()

# create_table = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id INT PRIMARY KEY, nome TEXT, \
# estrelas REAL, diaria REAL, cidade TEXT)"

create_hotel = "INSERT INTO hoteis VALUES (1, 'Pousada Belíssima', 5.0, 170.00, 'Serrinha/BA')"

cursor.execute(create_hotel)
# cursor.execute(create_table)
connection.commit()
connection.close()