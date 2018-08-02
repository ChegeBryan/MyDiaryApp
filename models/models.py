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
        return {
            'id': data[0],
            'username': data[1],
            'email': data[2],
            'password': data[3]
        }

    @staticmethod
    def generate_hash_password(password):
        """Method to encrypt password"""
        return sha256.hash(password)

    @staticmethod
    def verify_hash_password(password, hash):
        """Method to decrypt hash password"""
        return sha256.verify(password, hash)

class Entry:

    def __init__(self, title, journal):
        self.title = title
        self.journal = journal
        self.create_at = datetime.now()
        self.last_modified_at = datetime.now()

    def save_entry(self):
        """Method to save an entry into the database"""
        conn.commit()

    def add_entry(self):
        """Method to add an entry into the database"""
        sql = """INSERT INTO public.entries
                (user_id, title, journal, create_at, last_modified_at)
                VALUES('', '', '', '');"""
        cur = conn.cursor()
        cur.execute(sql, (self.title, self.journal, self.create_at, self.last_modified_at))
        self.save_entry()

    def get_entry_by_id(self):
        """Method to return an entry by the id passed"""
        pass

    def edit_entry(self):
        """Method to edit a specific entry"""
        pass

    def delete_entry(self):
        """Method to remove an entry from the database"""
        pass
