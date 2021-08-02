#!/usr/bin/env python3
import random
import sqlite3


"""
This module sets up the Restaurant Constructor and the function used to detirmine the pertinant Restaurant information.


"""


class Restaurant:

    @staticmethod
    def dollar_conversion_helper(dollar_input):
        if dollar_input >= 50:
            return 4
        elif 25 <  dollar_input < 50:
            return 3
        elif 10 < dollar_input <= 25:
            return 2
        else:
            return 1


    def __init__(self, dbname, min_cost_pref_dollars, max_cost_pref_dollars):

        if type(max_cost_pref_dollars) != int:
            raise TypeError("Hotel input 'max_price_pref' must be an int")

        if type(min_cost_pref_dollars) != int:
            raise TypeError("Hotel input 'min_price_pref' must be an int")

        if min_cost_pref_dollars <= 0:
            raise Exception("Restaurant input min_cost_pref_dollars must be greater than 0")
        
        if max_cost_pref_dollars <= 0:
            raise Exception("Restaurant input max_cost_pref_dollars must be greater than 0")

        if (type(dbname) != str):
            raise TypeError("Hotel input 'dbname' must be string")

        if min_cost_pref_dollars > max_cost_pref_dollars:
            raise Exception("Restaurant input 'max_cost_pref_dollars' must be greater than min_cost_pref_dollars")

        min_cost_pref = self.dollar_conversion_helper(min_cost_pref_dollars)
        max_cost_pref = self.dollar_conversion_helper(max_cost_pref_dollars)

        self.name = "N/A"
        self.max_cost_pref_dollars = max_cost_pref_dollars
        self.min_cost_pref_dollars = min_cost_pref_dollars
        self.max_cost_pref = max_cost_pref
        self.min_cost_pref = min_cost_pref
        self.cost = 0
        self.address = "N/A"
        self.phone = 0
        self.database = dbname


    def pick_restaurant(self):
        conn = sqlite3.connect(self.database)
        curr = conn.cursor()

        query = """SELECT * from Restaurant"""
        curr.execute(query)
        records = curr.fetchall()
        shuffled_records = random.sample(records, len(records))
        for row in shuffled_records:
            if row[4] <= self.max_cost_pref and row[4] >= self.min_cost_pref:
                self.name = row[1]
                self.address = row[2]
                self.phone = row[3]
                self.cost = row[4] 
                conn.commit()
                conn.close()
                return               
        conn.commit()
        conn.close()
