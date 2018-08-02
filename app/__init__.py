"""Creation of flask object"""
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import config_environment
from models.create_db import connect_to_db

app = Flask(__name__, instance_relative_config=True)
config_name = os.getenv('APP_SETTINGS')
app.config['JWT_SECRET_KEY'] = 'my_precious'
app.config.from_object(config_environment[config_name])
app.config.from_pyfile('config.py')
conn = connect_to_db()
jwt = JWTManager(app)

from app import entries
from app import users
