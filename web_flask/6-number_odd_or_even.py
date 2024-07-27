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


@app.route('/number/<int:n>', strict_slashes=False)
def only_digits_dynamic(n=None):
    """Dynamic inputted integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n=None):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_two(n=None):
    """Renders a page after deciding if n is odd or even"""
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('templates/6-number_odd_or_even.html', number=n, outcome=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
