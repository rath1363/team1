
#
# Team 1
# My Weekend in Miami
#

import sqlite3
import random

"""

PURPOSE:
Used by the Itinerary class to select activities for the user from a database
of activities based on the user's maximum funds available for activities.
This class then stores these selections to make them available to the
Itinerary class.

The user will be in Miami from Friday afternoon through Sunday afternoon.
There will therefore be no Friday morning activity nor any Sunday evening
actvitiy. The Friday afternoon activity will be the user's arrival in Miami
and the Sunday afternoon activity will be the user's departure from Miami.
The five remaining values must be set by the program based on the user's
preferences:

    Friday Evening
    Saturday Morning
    Saturday Afternoon
    Saturday Evening
    Sunday Morning


"""


class Activities:

    def __init__(self, activities_budget, dbname):
        """
        Activities Constructor
            Parameters:
                activities_budget (int)
                    maximum dollar amt (per person) available for activities
                dbname (str)
                    name of database containing activities to choose from
            Return:
                Activities instance
        """
        # Type-check 'activities_budget' parameter
        if (type(activities_budget) != int):
            raise TypeError("Activities param 'activities_budget' must be int")
        self.activities_budget = activities_budget

        # Type-check 'dbname' parameter
        if (type(dbname) != str):
            raise TypeError("Activities param 'dbname' must be string")
        self.dbname = dbname

        # Initialize activities itinerary attributes
        self.friday_mor   = "N/A"
        self.friday_aft   = "Arrival in Miami"
        self.friday_eve   = ""
        self.saturday_mor = ""
        self.saturday_aft = ""
        self.saturday_eve = ""
        self.sunday_mor   = ""
        self.sunday_aft   = "Departure from Miami"
        self.sunday_eve   = "N/A"


    # Helper method for pick_activities_helper method
    #   Deprecated -- replaced by select_activity_rand()
    def select_activity(self, max_price, activity_list):
        for activity in activity_list:
            if (int(activity[8]) <= max_price):
                return activity
        raise Exception("No match found in Activities.select_activity method")


    # Helper method for pick_activities_helper method
    #   This is a randomized version of the select_activity method
    def select_activity_rand(self, max_price, activity_list):
        act = random.choice(activity_list)
        act_price = int(act[8])
        while (act_price > max_price):
            act = random.choice(activity_list)
            act_price = int(act[8])
        return act


    # Helper method for pick_activities method
    def pick_activities_helper(self, activity_list):
        search_list = activity_list
        ret_list    = []

        # Get first activity
        available_balance = self.activities_budget
        item_max = available_balance / 5
        activity = self.select_activity_rand(item_max, search_list)
        activity_price = int(activity[8])
        ret_list.append(activity)
        search_list.remove(activity)

        # Get second activity
        available_balance -= activity_price
        item_max = available_balance / 4
        activity = self.select_activity_rand(item_max, search_list)
        activity_price = int(activity[8])
        ret_list.append(activity)
        search_list.remove(activity)

        # Get third activity
        available_balance -= activity_price
        item_max = available_balance / 3
        activity = self.select_activity_rand(item_max, search_list)
        activity_price = int(activity[8])
        ret_list.append(activity)
        search_list.remove(activity)

        # Get fourth activity
        available_balance -= activity_price
        item_max = available_balance / 2
        activity = self.select_activity_rand(item_max, search_list)
        activity_price = int(activity[8])
        ret_list.append(activity)
        search_list.remove(activity)

        # Get fifth activity
        available_balance -= activity_price
        item_max = available_balance
        activity = self.select_activity_rand(item_max, search_list)
        activity_price = int(activity[8])
        ret_list.append(activity)
        search_list.remove(activity)

        return ret_list


    # Populates empty Activites attributes
    def pick_activities(self):
        # Connect to database
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        # Retrieve activities data from database
        output_ptr = c.execute("SELECT * FROM Entertainment;")
        output_lst = output_ptr.fetchall()

        # Retrieve list of suitable activities and populate empty
        #   activities attributes
        activity_list = self.pick_activities_helper(output_lst)
        self.friday_eve   = activity_list[0]
        self.saturday_mor = activity_list[1]
        self.saturday_aft = activity_list[2]
        self.saturday_eve = activity_list[3]
        self.sunday_mor   = activity_list[4]

        # Save and close database
        conn.commit()
        conn.close()


        """
        activity_list KEY to determine output

        first index
        0 : Friday evening
        1 : Saturday morning
        2 : Saturday afternoon
        3 : Saturday evening
        4 : Sunday morning

        second index
        0 : Entertainment ID
        1 : Description
        2 : Includes
        3 : Contact
        4 : Street Address
        5 : City
        6 : State
        7 : Zip
        8 : Price Per Person
        9 : Price Total
        10: Phone Number
        11: Google Rating
        12: URL
        13: Opening Time
        14: Closing Time
        15: Morning	        Boolean: open in the mornings?
        16: Afternoon       Boolean: open in the afternoons?
        17: Evening	        Boolean: open in the evenings?
        18: Child Friendly  Boolean: can children participate?
        """
