#!/usr/bin/python3
"""
Initiates a Flask-based web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """ Eliminates the current SQLAlchemy session."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all state objects
    present in DBStorage."""
    states = storage.all(state).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted.states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
