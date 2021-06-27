#!/usr/bin/env python3

#
# Installed packages:
# 
#

from flask import (Flask, redirect, render_template, url_for)
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/welcome')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/budget')
def budget():
    return render_template('budget.html')


@app.route('/lodging')
def lodging():
    return render_template('lodging.html')


@app.route('/meals')
def meals():
    return render_template('meals.html')


@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')


@app.route('/itinerary')
def itinerary():
    return render_template('itinerary.html')


if __name__ == '__main__':
    app.run(debug=True)
