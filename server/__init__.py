import logging
import os

import flask
from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config.default")
app.config.from_pyfile("config.py")

# setup logger
from . import flask_log_handlers

app.logger.removeHandler(flask.logging.default_handler)
log_file_dir = os.path.join(os.getcwd(), ".log")
flask_log_handlers.logger_setup(
    name=app.logger.name, log_file_dir=log_file_dir, log_file_level=logging.DEBUG
)

# define routes
from server import routes

# setup datastore
from server import models

# define controllers
from server import controllers

