import psycopg2


def connect_to_db():
    conn = psycopg2.connect(database='my_diary_test',
                            user='postgres', password='12345qwerty',
                            host='localhost', port='5432')

    print('Opened database successfully')

    return conn


def create_user_tbl():

    cur.execute('''CREATE TABLE users(
      id serial PRIMARY KEY,
      username VARCHAR NOT NULL UNIQUE,
      email VARCHAR NOT NULL UNIQUE,
      password VARCHAR NOT NULL);''')

    print('Entries table created')


def create_entries_tbl():

    cur.execute('''CREATE TABLE entries(
        id serial,
        user_id INTEGER NOT NULL,
        title VARCHAR NOT NULL,
        journal VARCHAR NOT NULL,
        create_at timestamp NOT NULL,
        last_modified_at timestamp NOT NULL,
        PRIMARY KEY (user_id, id),
        FOREIGN KEY (user_id) REFERENCES users (id));''')

    print('Entries table created success')


if __name__ == '__main__':
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS users CASCADE ''')
    cur.execute('''DROP TABLE IF EXISTS entries CASCADE ''')
    create_user_tbl()
    create_entries_tbl()

    cur.close()
    conn.commit()
    conn.close()
    print('database created successfully')