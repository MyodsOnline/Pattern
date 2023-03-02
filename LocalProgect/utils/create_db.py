import sqlite3
import os

# db_file = os.path.join('..', 'db.sqlite')

db_connection = sqlite3.connect('db.sqlite')
db_cursor = db_connection.cursor()

with open('create_db.txt', 'r') as f:
    text = f.read()
    print(text)

db_cursor.executescript(text)

db_cursor.close()
db_connection.close()
