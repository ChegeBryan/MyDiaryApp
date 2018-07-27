from .create_db import connect_to_db

conn = connect_to_db()


class User:
    """"Defines the user model"""

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def add_user(self):
        """Adds user new user db user"""
        sql = """INSERT INTO users(username, email, password) VALUES(%s,%s,%s);"""
        cur = conn.cursor()
        cur.execute(sql, (self.username, self.email, self.password))
        conn.commit()

    def get_users(self):
        """Method to read the user table and return the users"""
        sql = """SELECT * FROM users"""
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data






class  Entries():

