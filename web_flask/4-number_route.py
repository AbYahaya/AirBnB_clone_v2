#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A basic flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns the hbnb page"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text variable"""
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """Dynamically generated route, with space replacing underscores"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
     """Handles the route /number/<n> only if n is an integer"""
     return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
