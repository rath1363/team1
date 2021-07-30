#!/usr/bin/env python3
import random
import sqlite3


"""
This module sets up the Restaurant Constructor and the function used to detirmine the pertinant resturaunt information.


"""

class Restaurant:
    def __init__(self, dbname, min_cost_pref, max_cost_pref):

        if type(max_cost_pref) != int:
            raise TypeError("Hotel input 'max_price_pref' must be an int")

        if type(min_cost_pref) != int:
            raise TypeError("Hotel input 'min_price_pref' must be an int")

        if (type(dbname) != str):
            raise TypeError("Hotel input 'dbname' must be string")

        if max_cost_pref > 4:
            raise Exception("Resturaunt input 'max_cost_pref' must be 4 or lower")

        if max_cost_pref < 1:
            raise Exception("Resturaunt input 'max_cost_pref' must be 1 or greater")

        if min_cost_pref > 4:
            raise Exception("Resturaunt input 'max_cost_pref' must be 4 or lower")

        if min_cost_pref < 1:
            raise Exception("Resturaunt input 'max_cost_pref' must be 1 or greater")

        if min_cost_pref > max_cost_pref:
            raise Exception("Resturaunt input 'max_cost_pref' must be greater than min_cost_pref")

        self.name = "N/A"
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


