import os
from flask import Flask
import flask
from server import app
import server.controllers


@app.route("/index/")
@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/graph-demo/")
def graph_example():
    import bokeh.plotting as bpl
    import bokeh.models as bmo
    import bokeh.layouts as bla
    import bokeh.io as bio
    import bokeh.resources as bre
    import bokeh.embed as bem
    import bokeh.themes as bth
    import numpy as np

    # prepare some data
    N = 100
    x = np.linspace(0, 4 * np.pi, N)
    y0 = np.sin(x)
    y1 = np.cos(x)
    y2 = np.sin(x) + np.cos(x)

    # specify dimensions
    w, h = (400, 400)

    # create a plots w/ shared ranges
    s1 = bpl.figure(width=w, plot_height=h, title=None)
    s1.circle(x, y0, size=10, color="navy", alpha=0.5)
    s1.sizing_mode = "scale_both"
    s2 = bpl.figure(
        width=w, height=h, x_range=s1.x_range, y_range=s1.y_range, title=None
    )
    s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)
    s2.sizing_mode = "scale_both"
    s3 = bpl.figure(width=w, height=h, x_range=s1.x_range, title=None)
    s3.square(x, y2, size=10, color="olive", alpha=0.5)
    s3.sizing_mode = "scale_both"
    p = bla.gridplot([[s1, s2, s3]])
    p.sizing_mode = "scale_both"

    # save the results to a static HTML file
    # bokeh_tmp_html_path = os.path.join(app.root_path, "tmp", "bokeh.html")
    bokeh_template = app.jinja_env.get_template("bokeh.html")
    html = bem.file_html(
        p, resources=bre.CDN, template=bokeh_template, theme=bth.LIGHT_MINIMAL
    )

    # return flask.render_template("bokeh.html", bokeh_html=flask.Markup(html))
    return flask.Markup(html)
