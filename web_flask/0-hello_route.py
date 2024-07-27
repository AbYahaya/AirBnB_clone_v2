#!/usr/bin/python3
from flask import Flask
""""
A script that starts a flask app
"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """defines the home route"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
