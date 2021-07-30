
#
# Team 1
# My Weekend in Miami
#


"""

PURPOSE:
Module that takes in the maximum amount a user wants to spend per person
on their weekend in Miami and outputs a general breakdown of the trip
budget according to the following protocol:

    Transportation: 33%
    Accomodations:  33%
    Activities:     15%
    Meals:          11%
    Other:           8%

Source for recommended budget breakdown:
"How to Create a Family Vacation Budget" by Abby Hayes
Available at:
https://www.doughroller.net/smart-spending/budgeting-family-travel/


"""


class Budget:

    def __init__(self, maxbudget):
        """
        Budget Constructor
            Parameter: maxbudget (int)
                maximum (per person) user is willing to spend on their vacation
            Return:
                Budget instance
        """
        if (type(maxbudget) != int):
            raise TypeError("parameter 'maxbudget' must be integer")

        self.transportation = int(maxbudget * 0.33)
        self.accomodations = int(maxbudget * 0.33)
        self.activities = int(maxbudget * 0.15)
        self.meals = int(maxbudget * 0.11)
        self.other = int(maxbudget * 0.08)
        self.total = int(maxbudget)
