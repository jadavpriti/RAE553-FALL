import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()


create_table = ('''CREATE TABLE IF NOT EXISTS users (id INTEGER,name text NOT NULL,password text NOT NULL)''')
cursor.execute(create_table)

users = [
(1, 'priti', '12345'),
(2, 'bob', '12346'),
(3, 'eva', '12348')
]

insert_query = ("INSERT INTO users VALUES (?, ?, ?)")

for i in users:
    cursor.execute(insert_query, (i))
connection.commit()

connection.close()

print(users)
