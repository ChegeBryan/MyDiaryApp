import psycopg2


def connect_to_db():
    create_connection = psycopg2.connect(database='my_diary_test',
                                         user='postgres', password='12345qwerty',
                                         host='localhost', port='5432')

    print('Opened database successfully')

    return create_connection


def create_user_tbl():
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
      id serial PRIMARY KEY,
      username VARCHAR NOT NULL UNIQUE,
      email VARCHAR NOT NULL UNIQUE,
      password VARCHAR NOT NULL);''')

    print('Entries table created')


def create_entries_tbl():
    cur.execute('''CREATE TABLE IF NOT EXISTS entries (
        id serial,
        user_id INTEGER NOT NULL,
        title VARCHAR NOT NULL,
        journal VARCHAR NOT NULL,
        create_at timestamp NOT NULL,
        last_modified_at timestamp,
        PRIMARY KEY (user_id, id),
        FOREIGN KEY (user_id) REFERENCES users (id));''')

    print('Entries table created success')


conn = connect_to_db()
cur = conn.cursor()
create_user_tbl()
create_entries_tbl()
cur.close()
conn.commit()
conn.close()
print('database created successfully')
