#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template, g
import models
from models.state import State

app = Flask(__name__, template_folder='templates')


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ displays a list of all the states"""
    states = models.storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(error):
    """ removes the current SQLAlchemy Session after
    each request """
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
