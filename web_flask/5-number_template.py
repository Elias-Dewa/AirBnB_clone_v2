#!/usr/bin/python3
""" a script that starts a Flask web application:
the web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays a give string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a given string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays C followed by the value of text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
