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


def states():
    """ Display list of all the states """
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('9-states.html', states=states_list, id=None)


@app.route('/states')
@app.route('/states/<id>')
def statesWithID(id):
    """ Display list of all the states """
    states = storage.all(State)
    states_list = list(states.values())
    for state in states_list:
        if isinstance(state, State) and id == state.id:
            cities = state.cities
    return render_template('9-states.html', state=state, cities=cities, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
