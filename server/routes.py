import flask
from server import app


@app.route("/index/")
@app.route("/")
def index():
    return flask.render_template("index.html")
