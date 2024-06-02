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


@app.route('/states')
def states():
    """ Display list of all the states """
    states = storage.all(State)
    return render_template('9-states.html', state=states)


@app.route('/states/<id>')
def statesWithID(id):
    """ Display list of all the states """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
