#!/usr/bin/python3
""" This module starts a Flask web application with 2 routes """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def try_this():
    """ This function displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This function displays 'HBNB!' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    """ Prints value of text variable - C """
    return 'C %s' % (text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_py(text="is cool"):
    """ Prints value of text variable - Python """
    return 'Python %s' % (text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def print_ints(n):
    """ Prints ints only """
    return '%d is a number' % (n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_html(n=None):
    """ This function displays an html tag for ints only """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_html_oddeve(n=None):
    """ This function displays an odd or even html tag for ints only """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
