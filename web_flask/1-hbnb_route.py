#!/usr/bin/python3
""" This module starts a Flask web application with 2 routes """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def try_this():
    """ This function displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This function displays 'HBNB!' """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
