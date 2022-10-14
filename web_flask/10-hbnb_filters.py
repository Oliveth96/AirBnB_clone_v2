#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
import models
from models.state import State
from models.amenity import Amenity

app = Flask(__name__, template_folder='templates')


@app.route('/hbnb_filters', strict_slashes=False)
def render_html():
    """view that lists all of the states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states.values(),
                           amenities=amenities.values())


@app.teardown_appcontext
def tear_down(error):
    """ removes the current SQLAlchemy Session after
    each request """
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)