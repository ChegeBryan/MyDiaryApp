from datetime import datetime, timedelta
from .create_db import connect_to_db
import jwt
import psycopg2.extras as extras
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
        return data

    @staticmethod
    def get_user_by_email(email):
        """Method to get user by id to enable token generation"""
        sql = """SELECT * FROM users WHERE email=(%s)"""
        cur = conn.cursor()
        cur.execute(sql, (email,))
        user = cur.fetchone()
        return user

    def generate_auth_token(self, user_id):
        """
        Generates the authentication token
        :param user_id:
        :return token string:
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(seconds=21600),
                'iat': datetime.utcnow(),
                'sub': user_id,
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        decode the auth token
        :param auth_token:
        :return integer|string:
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again'


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
