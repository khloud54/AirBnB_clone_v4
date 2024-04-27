#!/usr/bin/python3
"""places_reviews"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.review import Review
from datetime import datetime
import uuid



@app_views.route('/places/<place_id>/reviews', methods=['GET'])
@app_views.route('/places/<place_id>/reviews', methods=['GET'])
