from datetime import datetime, timedelta
from .create_db import connect_to_db
import jwt
from app import app

conn = connect_to_db()

"""
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

    @staticmethod
    def get_users():
        """Method to read the user table and return the users"""
        sql = """SELECT * FROM users"""
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data


    def generate_auth_token(user_id):
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

