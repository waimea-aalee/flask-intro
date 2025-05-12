from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("pages/home.jinja")


@app.get("/test/")
def test():
    return "<h1>Testing... 1, 2, 3</h1>"

@app.get("/two/")
def two():
    return render_template("pages/two.jinja")

@app.get("/about/")
def about():
    return render_template("pages/about.jinja")