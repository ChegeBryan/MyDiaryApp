"""Creation of flask object"""
import os
from flask import Flask
from instance.config import config_environment

app = Flask(__name__, instance_relative_config=True)
config_name = os.getenv('APP_SETTINGS')
app.config.from_object(config_environment[config_name])
app.config.from_pyfile('config.py')

from app import api
