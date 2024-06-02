#!/usr/bin/python3
"""script that starts a Flask web application."""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def homePage():
    """Function that display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnbPage():
    """Function that display “HBNB” """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
