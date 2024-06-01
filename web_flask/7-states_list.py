#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def dispose(exception):
    """ Remove current session """
    storage.close()


@app.route('/states_list')
def states():
    """ Display list of all the states """
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
