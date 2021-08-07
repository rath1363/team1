
#
# Team 1
# My Weekend in Miami
#

import budget
import hotel_setup
import activities
import restaurant_setup
import db           # Used to build temporary database
import os           # Used to delete temporary database

"""

PURPOSE:
Module that takes in the maximum amount a user wants to spend per person
on their weekend in Miami and outputs a weekend itinerary that satisfies these
budget constraints.

This module calls on the Budget, Hotel, Activties, and Meals modules. An
instance of each of these classes is a member attribute of each instance of
the Itinerary class.


"""


class Itinerary:

    def __init__(self, maxbudget):
        """
        Itinerary Constructor
            Parameter: maxbudget (int)
                maximum (per person) user is willing to spend on their vacation
            Return:
                Itinerary instance
        """
        # Determine budget
        trip_budget = budget.Budget(maxbudget)

        # Initialize temporary database
        dbname = "temporary.db"
        db.create(dbname)
        db.parseLodging(dbname)
        db.parseEnt(dbname)
        db.parseRest(dbname)

        # Choose hotel
        hotel = hotel_setup.Hotel(dbname, trip_budget.accomodations, 1)
        hotel.pick_hotel()
        self.hotel = hotel

        # Choose entertainment
        ent = activities.Activities(trip_budget.activities, dbname)
        ent.pick_activities()
        self.ent = ent

        # Choose restaurants
        rest = restaurant_setup.Restaurant(dbname, 1, trip_budget.meals)
        restLst = rest.pick_restaurant()
        self.meals = restLst

        # Set expenses attributes
        self.hotel_exp = self.hotel.cost * 2
        self.ent_exp   = (self.ent.friday_eve[8] + self.ent.saturday_mor[8] +
                          self.ent.saturday_aft[8] + self.ent.saturday_eve[8] +
                          self.ent.sunday_mor[8])
        self.meals_exp = (self.get_rest_price(self.meals[0][4]) +
                          self.get_rest_price(self.meals[1][4]) +
                          self.get_rest_price(self.meals[2][4]) +
                          self.get_rest_price(self.meals[3][4]) +
                          self.get_rest_price(self.meals[4][4]))
        self.total_exp = self.hotel_exp + self.ent_exp + self.meals_exp

        # Delete temporary database
        if os.path.exists("temporary.db"):
            os.remove("temporary.db")
        else:
            errMsg  = " -- Anamolous Behavior Warning -- \n"
            errMsg += "Itinerary tried to remove temporary.db "
            errMsg += "but file does not exist.\n"
            raise Exception(errMsg)


    def get_rest_price(self, rest_price):
        if (rest_price == 1):
            return 10
        elif (rest_price == 2):
            return 25
        elif (rest_price == 3):
            return 50
        else:
            return 65


    def get_itinerary_str(self):
        output  = f"-- Itinerary -- \n\n"
        output += f"Hotel: {self.hotel.name}\n"
        output += f"       ${self.hotel.cost} per night\n"
        output += f"       ${self.hotel.cost * 2} total\n\n"
        output += f"Friday \n"
        output += f"    Activities: \n"
        output += f"        Morning:   N/A \n"
        output += f"        Afternoon: Arrival \n"
        output += f"        Evening:   {self.ent.friday_eve[1]}\n"
        output += f"                   ${self.ent.friday_eve[8]}\n"
        output += f"                   {self.ent.friday_eve[12]}\n"
        output += f"    Meals: \n"
        output += f"        Dinner:    {self.meals[0][1]} \n"
        output += f"                   ${self.get_rest_price(self.meals[0][4])}\n"
        output += f"Saturday \n"
        output += f"    Activities: \n"
        output += f"        Morning:   {self.ent.saturday_mor[1]}\n"
        output += f"                   ${self.ent.saturday_mor[8]}\n"
        output += f"                   {self.ent.saturday_mor[12]}\n"
        output += f"        Afternoon: {self.ent.saturday_aft[1]}\n"
        output += f"                   ${self.ent.saturday_aft[8]}\n"
        output += f"                   {self.ent.saturday_aft[12]}\n"
        output += f"        Evening:   {self.ent.saturday_eve[1]}\n"
        output += f"                   ${self.ent.saturday_eve[8]}\n"
        output += f"                   {self.ent.saturday_eve[12]}\n"
        output += f"    Meals: \n"
        output += f"        Breakfast: {self.meals[1][1]} \n"
        output += f"                   ${self.get_rest_price(self.meals[1][4])}\n"
        output += f"        Lunch:     {self.meals[2][1]} \n"
        output += f"                   ${self.get_rest_price(self.meals[2][4])}\n"
        output += f"        Dinner:    {self.meals[3][1]} \n"
        output += f"                   ${self.get_rest_price(self.meals[3][4])}\n"
        output += f"Sunday \n"
        output += f"    Activities:    \n"
        output += f"        Morning:   {self.ent.sunday_mor[1]}\n"
        output += f"                   ${self.ent.sunday_mor[8]}\n"
        output += f"                   {self.ent.sunday_mor[12]}\n"
        output += f"        Afternoon: Departure \n"
        output += f"        Evening:   N/A \n"
        output += f"    Meals: \n"
        output += f"        Breakfast: {self.meals[4][1]} \n"
        output += f"                   ${self.get_rest_price(self.meals[4][4])}\n"
        output += f"        Lunch:     N/A \n"
        output += f"        Dinner:    N/A \n"

        return output


    def get_expenses_str(self):
        output  = f"-- Expenses -- \n\n"
        output += f"Lodging: ${self.hotel_exp}\n"
        output += f"Meals:   ${self.meals_exp}\n"
        output += f"Entertainment: ${self.ent_exp}\n\n"
        output += f"TOTAL: ${self.total_exp}\n"

        return output
