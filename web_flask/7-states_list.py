#!/usr/bin/python3
""" a script that starts a Flask web application:
the web application must be listening on 0.0.0.0, port 5000
"""
from models.state import State
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Displays a HTML page with a list of State
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(self):
    """To close the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
