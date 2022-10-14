#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_Flask():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c():
    """Displays C message"""
    text = text.replace('_', " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
