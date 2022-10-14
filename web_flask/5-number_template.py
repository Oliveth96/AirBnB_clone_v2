#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', strict_slashes=False)
def hello_Flask():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Displays C message"""
    text = text.replace('_', " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def display_python(text='is cool'):
    """ Displays 'python' followed by the text"""
    text = text.replace('_', " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_integer(n):
    """ Displays n, if it is an int."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_HTML(n):
    """ displays HTML only if n is int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
