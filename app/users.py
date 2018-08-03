import re

from flask import request, jsonify
from app import app
from flask.views import MethodView
from models.models import User
from flask_jwt_extended import create_access_token, create_refresh_token


class UserRegistration(MethodView):
    """User registration route"""
    def post(self):
        request_data = request.get_json()
        if 'username' not in request_data:
            return jsonify({'message': 'missing username in json request'}), 400
        if 'email' not in request_data:
            return jsonify({'message': 'missing email in json request'}), 400
        if 'password' not in request_data:
            return jsonify({'message': 'missing password in json request'}), 400
        if 'username' in request_data and not request_data['username'].strip():
            return jsonify({'message': 'title cannot be empty'}), 400
        if 'email' in request_data and not request_data['email'].strip():
            return jsonify({'message': 'journal cannot be empty'}), 400
        if not re.match('[^@]+@[^@]+\.[^@]+',request_data['email']):
            return jsonify({'message': 'email not valid'}), 400
       username = request_data['username']
        email = request_data['email']
        password = User.generate_hash_password(request_data['password'])
        user = User(username=username, email=email, password=password)
        user.add_user()
        return jsonify({'message': 'user created'}), 201


class UserLogin(MethodView):
    """User log-in route"""
    def post(self):
        request_data = request.get_json()
        if 'username' and 'password' not in request_data:
            return jsonify({'message': 'Provide all the necessary credentials'}), 404
        if len(request_data['username']) > 4:
            user_candidate = request_data['username']
            try:
                user = User.get_user_by_username(user_candidate)
                if user['username'] == user_candidate:
                    password_candidate = request_data['password']
                    user_password = user['password']
                    if User.verify_hash_password(password_candidate, user_password):
                        access_token = create_access_token(identity=user['id'])
                        refresh_token = create_refresh_token(identity=user['id'])
                        return jsonify({'message': 'log in success',
                                        'access_token': access_token,
                                        'refresh_token': refresh_token
                                        }), 200
                    else:
                        return jsonify({'message': 'Log in unsuccessful'}), 404
            except:
                return jsonify({'message': 'Log in unsuccessful'})
        else:
            return jsonify({'Message': 'username must satisfy the minimum length'}), 400


class UserLogout(MethodView):
    pass


user_registration = UserRegistration.as_view('user_signup')
user_login = UserLogin.as_view('user_login')
app.add_url_rule('/auth/signup', view_func=user_registration, methods=['POST'])
app.add_url_rule('/auth/login', view_func=user_login, methods=['POST'])

