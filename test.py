#!/usr/bin/env python3

#
# Team 1
# My Weekend in Miami
#


"""

Tests Budget and Activities modules.

Instructions:
    - Download all files in root directory for 'team1' project.
    - In terminal, navigate to this root directory.
    - Execute this file in terminal:
        ~$ ./test.py

"""

import unittest
import budget
import activities

class BudgetTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Test Budget init method
    def test_init(self):
        test_max = 1200
        test_trip = budget.Budget(test_max)
        self.assertEqual(test_trip.transportation, test_max * 0.33,
            "Error in Budget init attribute: transportation")
        self.assertEqual(test_trip.accomodations, test_max * 0.33,
            "Error in Budget init attribute: accomodations")
        self.assertEqual(test_trip.activities, test_max * 0.15,
            "Error in Budget init attribute: activities")
        self.assertEqual(test_trip.meals, test_max * 0.11,
            "Error in Budget init attribute: meals")
        self.assertEqual(test_trip.other, test_max * 0.08,
            "Error in Budget init attribute: other")
        self.assertEqual(test_trip.total, test_max,
            "Error in Budget init attribute: total")

    # Budget init method should raise TypeError if passed non-int
    def test_non_int_input_to_constructor(self):
        string_val = "not an int"
        float_val = 1200.1200
        self.assertRaises(TypeError, budget.Budget, string_val)
        self.assertRaises(TypeError, budget.Budget, float_val)


class ActivitiesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Test Activities init method
    def test_init(self):
        test_budget = 180
        test_activities = activities.Activities(test_budget)
        self.assertEqual(test_activities.activities_budget, test_budget,
            "Error in Activities init attribute: activities_budget")
        self.assertEqual(test_activities.friday_mor, "N/A",
            "Error in Activities init attribute: friday_mor")
        self.assertEqual(test_activities.friday_aft, "Arrival in Miami",
            "Error in Activities init attribute: friday_aft")
        self.assertEqual(test_activities.friday_eve, "",
            "Error in Activities init attribute: friday_eve")
        self.assertEqual(test_activities.saturday_mor, "",
            "Error in Activities init attribute: saturday_mor")
        self.assertEqual(test_activities.saturday_aft, "",
            "Error in Activities init attribute: saturday_aft")
        self.assertEqual(test_activities.saturday_eve, "",
            "Error in Activities init attribute: saturday_eve")
        self.assertEqual(test_activities.sunday_mor, "",
            "Error in Activities init attribute: sunday_mor")
        self.assertEqual(test_activities.sunday_aft, "Departure from Miami",
            "Error in Activities init attribute: sunday_aft")
        self.assertEqual(test_activities.sunday_eve, "N/A",
            "Error in Activities init attribute: sunday_eve")

    # Activities init method should raise TypeError if passed non-int
    def test_non_int_input_to_constructor(self):
        string_val = "not an int"
        float_val = 180.180
        self.assertRaises(TypeError, activities.Activities, string_val)
        self.assertRaises(TypeError, activities.Activities, float_val)


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
