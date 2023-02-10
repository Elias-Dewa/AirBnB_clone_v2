#!/usr/bin/python3
""" a script that starts a Flask web application:
the web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of text
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
