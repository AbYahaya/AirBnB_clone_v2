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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
