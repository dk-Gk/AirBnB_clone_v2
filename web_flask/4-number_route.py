#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display message to user"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display message to user"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_var(text):
    """display message to user"""
    return 'C %s' % escape(text.replace('_', ' '))


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def py_var(text, strict_slashes=False):
    """display message to user"""
    return 'Python  %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num_var(n):
    """display message to user"""
    return '%d is a number' % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
