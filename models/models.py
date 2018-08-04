from datetime import datetime, timedelta
from .create_db import connect_to_db
from passlib.hash import pbkdf2_sha256 as sha256
conn = connect_to_db()


class User:
    """"Defines the user model"""

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def add_user(self):
        """Adds user new user db user"""
        sql = """INSERT INTO users(username, email, password) VALUES(%s,%s,%s)"""
        cur = conn.cursor()
        cur.execute(sql, (self.username, self.email, self.password))
        conn.commit()

    @staticmethod
    def get_user_by_username(username):
        """Method to read the user table and return the users"""
        sql = """SELECT * FROM users WHERE username=%s"""
        cur = conn.cursor()
        cur.execute(sql, (username,))
        data = cur.fetchone()
        if data:
            return {
                'id': data[0],
                'username': data[1],
                'email': data[2],
                'password': data[3]
            }
        else:
            return None

    @staticmethod
    def get_user_by_email(email):
        """Method to read the user table and return the users"""
        sql = """SELECT * FROM users WHERE email=%s"""
        cur = conn.cursor()
        cur.execute(sql, (email,))
        data = cur.fetchone()
        if data:
            return {
                'id': data[0],
                'username': data[1],
                'email': data[2],
                'password': data[3]
            }
        else:
            return None

    @staticmethod
    def generate_hash_password(password):
        """Method to encrypt password"""
        return sha256.hash(password)

    @staticmethod
    def verify_hash_password(password, hash):
        """Method to decrypt hash password"""
        return sha256.verify(password, hash)

class Entry:

    def __init__(self, title, journal, user_id):
        self.title = title
        self.journal = journal
        self.user_id = user_id
        self.created_at = datetime.now()
        self.last_modified_at = datetime.now()


    def save_entry(self):
        """Method to save an entry into the database"""
        conn.commit()

    def add_entry(self):
        """Method to add an entry into the database"""
        sql = """INSERT INTO entries(user_id,title, journal,create_at,last_modified_at)
                VALUES(%s,%s,%s,%s,%s);"""
        cur = conn.cursor()
        cur.execute(sql, (self.user_id, self.title, self.journal, self.created_at,self.last_modified_at))
        self.save_entry()

    @staticmethod
    def get_entries(user_id):
        """Method to return all entries by a user"""
        sql = """SELECT * FROM entries WHERE user_id=%s"""
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        data = cur.fetchall()
        return data

    def get_entry_by_id(self):
        """Method to return an entry by the id passed"""
        pass

    def edit_entry(self):
        """Method to edit a specific entry"""
        pass

    def delete_entry(self):
        """Method to remove an entry from the database"""
        pass
