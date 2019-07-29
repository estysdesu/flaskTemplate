import os
from flask import Flask
import flask
from server import app
import server.controllers


@app.route("/index/")
@app.route("/")
def index():
    return flask.render_template("index.html")
