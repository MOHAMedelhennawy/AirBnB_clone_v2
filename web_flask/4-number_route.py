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


@app.route("/c/<text>", strict_slashes=False)
def cPage(text):
    """- display “C ” followed by the value of the text variable
       - (replace underscore _ symbols with a space )"""
    return "C {}".format(text).replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonPage(text='is cool'):
    """- display “Python ”, followed by the value of the text variable
       - (replace underscore _ symbols with a space )
       - The default value of text is “is cool”"""
    return "Python {}".format(text).replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def numberPage(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
