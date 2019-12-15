import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users(id int, username text, password text)"
cursor.execute(create_table)


user = (1, 'priti', '12345')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)
connection.commit()
