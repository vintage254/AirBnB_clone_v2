#!/usr/bin/python3
"""
starts a Flask web application
display “C ” followed by the value of the text variable
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Return string when route queried
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello_hbnb():
    """
    Return string when route queried
    """
    return 'HBNB'

@app.route('/c/<text>')
def c_display(text):
    """
    Return string when route queried
    """
    return 'c' + text.replace('_', ' ')

if __name___ = '__main__':
    app.url_map.strict_slashes=False
    app.run(host = '0.0.0.0', port = '5000')
