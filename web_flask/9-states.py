#!/usr/bin/python3
""" a script that starts a Flask web application:
the web application must be listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with a list of States
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Displays a HTML page with id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(self):
    """To close the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
