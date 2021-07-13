
#
# Team 1
# My Weekend in Miami
#


"""

PURPOSE:
Data structure to store the user's activities.

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

    def __init__(self, activities_budget):
        """
        Activities Constructor
            Parameter: maxbudget (int)
                maximum (per person) user is willing to spend on their vacation
            Return:
                Budget instance
        """

        if (type(activities_budget) != int):
            raise TypeError("parameter 'activities_budget' must be integer")

        self.activities_budget = activities_budget

        self.friday_mor   = "N/A"
        self.friday_aft   = "Arrival in Miami"
        self.friday_eve   = ""
        self.saturday_mor = ""
        self.saturday_aft = ""
        self.saturday_eve = ""
        self.sunday_mor   = ""
        self.sunday_aft   = "Departure from Miami"
        self.sunday_eve   = "N/A"
