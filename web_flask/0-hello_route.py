#!/user/bin/python3
"""
Code to launch a Flask-based wep application.
"""

from flask import Flask


app = Flask(__name__)
''' The instance of the Flask application. '''


@app.route('/', strict_slashes=False)
def hello_world():
    '''The main page.'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
