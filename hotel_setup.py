#!/usr/bin/env python3
import random
import sqlite3


"""
This module sets up the Hotel Constructor and the function used to detirmine the pertinant hotel information.

"""

class Hotel:
    def __init__(self, dbname, max_cost_pref, min_rating_pref):

        if type(max_cost_pref) != int:
            raise TypeError("Hotel input 'max_price_pref' must be an int")

        if type(min_rating_pref) != int:
            raise TypeError("Hotel input 'min_rating_pref' must be an int")

        if (type(dbname) != str):
            raise TypeError("Hotel input 'dbname' must be string")

        if min_rating_pref > 5:
            raise Exception("Hotel input 'min_rating_pref' must be 5 or lower")

        self.name = "N/A"
        self.rating_pref = min_rating_pref
        self.rating = 0
        self.cost_pref = max_cost_pref
        self.cost = 0
        self.address = "N/A"
        self.phone = 0
        self.database = dbname


    def pick_hotel(self):
        conn = sqlite3.connect(self.database)
        curr = conn.cursor()

        query = """SELECT * from Lodging"""
        curr.execute(query)
        records = curr.fetchall()
        shuffled_records = random.sample(records, len(records))
        for row in shuffled_records:
            if row[4] >= self.rating_pref:
                if row[5] <= self.cost_pref:                
                    self.name = row[1]
                    self.address = row[2]
                    self.phone = row[3]
                    self.rating = row[4]
                    self.cost = row[5]
                    conn.commit()
                    conn.close()
                    return

        conn.commit()
        conn.close()



