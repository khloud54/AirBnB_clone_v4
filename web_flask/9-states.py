#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    state = storage.get(State, state_id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
