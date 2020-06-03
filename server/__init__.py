import os
from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET

from flask import Flask
from flask.logging import default_handler
from flask_bootstrap import Bootstrap

from server import flask_log_handlers

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)

# setup config
app.config.from_object("config.default")
app.config.from_pyfile("config.py")

# setup logger
app.logger.removeHandler(default_handler)
log_file_dir = os.path.join(os.getcwd(), ".log")
flask_log_handlers.logger_setup(
    name=app.logger.name, log_file_dir=log_file_dir, log_file_level=INFO
)

# define routes
from server import routes

# setup datastore
from server import models

# define controllers
from server import controllers
