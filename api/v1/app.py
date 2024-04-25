#!/usr/bin/python3
"""app"""
from flask import Flask, make_response, jsonify
from os import getenv
from models import storage
from flask_cors import CORS
from api.v1.views import app_views



app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

app.url_map.strict_slashes = False
app.register_blueprint(app_views)



@app.teardown_appcontext
def tear(self):
    ''' shuts storage engine '''
    storage.close()

@app.errorhandler(404)
def not_found(error):
    ''' It manages the 404 error by delivering a JSON-formatted reply '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
