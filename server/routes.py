from flask import Flask
from server import app


@app.route("/index/")
@app.route("/")
def home():
    return "Hello, World!"

