from flask import request, jsonify, abort
from app import app
from flask.views import MethodView
from models.models import User


class UserRegistration(MethodView):

    def post(self):
        request_data = request.get_json()
        username = request_data['username']
        email = request_data['email']
        password = request_data['password']
        user = User(username=username, email=email, password=password)
        user.add_user()
        return jsonify({'message': 'user created'}), 201


class UserLogin(MethodView):

    def post(self):
        request_data = request.get_json()
        if 'username' and 'password' not in request_data:
            return jsonify({'message': 'Provide all the necessary credentials'}), 404
        if len(request_data['username']) > 4:
            user_candidate = request_data['username']
            user = User.get_user_by_username(user_candidate)
            if not user:
                return jsonify({'message': 'Log in unsuccessful'})
            if user['username'] == user_candidate:
                password_candidate = request_data['password']
                user_password = user['password']
                if password_candidate == user_password:
                    return jsonify({'message': 'log in success'}), 200
            else:
                return jsonify({'message': 'Log in unsuccessful'}), 404
        else:
            return jsonify({'Message': 'username must satisfy the minimum length'}), 400


class UserLogout(MethodView):
    pass

user_registration = UserRegistration.as_view('user_signup')
user_login = UserLogin.as_view('user_login')
app.add_url_rule('/auth/signup', view_func=user_registration, methods=['POST'])
app.add_url_rule('/auth/signup', view_func=user_registration, methods=['GET'])
app.add_url_rule('/auth/login', view_func=user_login, methods=['POST'])

