import psycopg2

conn = psycopg2.connect(database='my_diary_test',
                        user='postgres', password='12345qwerty',
                        host='localhost', port='5432')

print('Opened database successfully')

cur = conn.cursor()

cur.execute('''CREATE TABLE users(
id serial PRIMARY KEY,
username VARCHAR NOT NULL UNIQUE,
email VARCHAR NOT NULL UNIQUE,
password VARCHAR NOT NULL);''')

cur.execute('''CREATE TABLE entries(
id serial,
user_id INTEGER NOT NULL,
title VARCHAR NOT NULL,
journal VARCHAR NOT NULL,
create_at timestamp NOT NULL,
last_modified_at timestamp NOT NULL,
PRIMARY KEY (user_id, id),
FOREIGN KEY (user_id) REFERENCES users(id));''')

conn.commit()
conn.close()
print('Table create: success')
