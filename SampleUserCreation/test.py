import sqlite3

connection = sqlite3.connect('data.db') # connecting to the database

cursor = connection.cursor() # responsible for executing the query and storing the result

create_table = 'CREATE TABLE users (id int, username text, password text)'

cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'askd'),
    (3, 'anne', 'sfsfd')
]
cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM users' # retrieving data
for row in cursor.execute(select_query):
    print(row)

connection.commit() # saves the database with the new data

connection.close() # closes the database
