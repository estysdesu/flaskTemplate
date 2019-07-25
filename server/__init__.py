import logging
import os

import flask
from flask import Flask


app = Flask(__name__)

# setup logger
import server.flask_log_handlers

app.logger.removeHandler(flask.logging.default_handler)
log_file_dir = os.path.join(os.getcwd(), ".log")
server.flask_log_handlers.logger_setup(
    name=app.logger.name, log_file_dir=log_file_dir, log_file_level=logging.DEBUG
)

# define routes
from server import routes

# setup datastore
from server import models

# define controllers
from server import controllers
