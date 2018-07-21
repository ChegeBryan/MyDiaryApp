from flask import Flask
from instance.config import config_environment

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config_environment['development'])
app.config.from_pyfile('config.py')

from app import api
