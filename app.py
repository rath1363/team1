#!/usr/bin/env python3

#
# Installed packages:
# 
#

from flask import (Flask, redirect, render_template, url_for, request)

from budget import Budget
from hotel_setup import Hotel
from restaurant_setup import Restaurant
from activities import Activities
from itinerary import Itinerary

import db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/budget', methods=['POST'])
def budget():
    budget_amount = int(request.form.get('budget'))
    budget = Budget(budget_amount)
    itinerary = Itinerary(budget_amount)

    return render_template('itinerary.html', trip_budget=budget_amount, itinerary=itinerary)


@app.route('/itinerary')
def itinerary():
    return render_template('itinerary.html')


# 
@app.route('/lodging')
def lodging():
    return render_template('lodging.html')


@app.route('/meals')
def meals():
    return render_template('meals.html')


@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')

if __name__ == '__main__':
    app.run(debug=True)
