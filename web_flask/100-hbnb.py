#!/usr/bin/python3
""" a script that starts a Flask web application:
the web application must be listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the main HBnB filters HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(self):
    """To close the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
