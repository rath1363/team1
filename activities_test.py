#!/usr/bin/env python3

#
# Team 1
# My Weekend in Miami
#


"""

Tests Activities module.

Instructions:
    - Download all files in root directory for 'team1' project.
    - In terminal, navigate to this root directory.
    - Execute this file in terminal:
        ~$ ./activities_test.py

"""


import unittest
import activities


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
        test_db     = "test.db"
        test_activities = activities.Activities(test_budget, test_db)
        self.assertEqual(test_activities.activities_budget, test_budget,
            "Error in Activities init attribute: activities_budget")
        self.assertEqual(test_activities.dbname, "test.db",
            "Error in Activities init attribute: dbname")
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
    #   input for 'activities_budget' parameter
    def test_non_int_input_to_constructor(self):
        string_val = "not an int"
        float_val  = 180.180
        test_db    = "test.db"
        with self.assertRaises(TypeError) as te:
            activities.Activities(string_val, test_db)
        with self.assertRaises(TypeError) as te:
            activities.Activities(float_val, test_db)

    # Activities init method should raise TypeError if passed non-string
    #   input for 'dbname' parameter
    def test_non_int_input_to_constructor(self):
        test_budget = 180
        int_val     = 2
        float_val   = 2.21
        with self.assertRaises(TypeError) as te:
            activities.Activities(test_budget, int_val)
        with self.assertRaises(TypeError) as te:
            activities.Activities(test_budget, float_val)


    def test_select_activity(self):
        test_budget = 180
        test_db     = "test.db"
        test_activities = activities.Activities(test_budget, test_db)

        test_activities_list = build_activity_list()
        test_price = 10
        activity = test_activities.select_activity(test_price,
                                                   test_activities_list)
        self.assertEqual(activity, test_activities_list[3],
            "Error in Activities method select_activity")
        del test_activities_list[3]
        test_price = 25
        activity = test_activities.select_activity(test_price,
                                                   test_activities_list)
        self.assertEqual(activity, test_activities_list[3],
            "Error in Activities method select_activity")


    def test_select_activity_rand(self):
        test_budget = 180
        test_db     = "test.db"
        test_activities = activities.Activities(test_budget, test_db)

        test_activities_list = build_activity_list()
        test_price = 50
        activity = test_activities.select_activity_rand(test_price,
                                                        test_activities_list)
        self.assertFalse(activity == None)
        self.assertTrue(activity[8] <= test_price)


    def test_pick_activities_helper(self):
        # Create testable instance of Activities
        test_budget = 1650
        test_db     = "test.db"
        test_activities = activities.Activities(test_budget, test_db)

        # Feed this instance of Activties
        #   handbuilt input to test pick_activities_helper function.
        test_activities_list = build_activity_list()
        actual = test_activities.pick_activities_helper(test_activities_list)
        self.assertEqual(set(actual), set(build_activity_list()),
            "Error in Activities method pick_activities_helper")


    def test_pick_activities(self):
        test_budget = 1650
        test_db     = "activities_test.db"
        test_activities = activities.Activities(test_budget, test_db)
        test_activities.pick_activities()
        self.assertTrue(test_activities.friday_eve != "")
        self.assertTrue(test_activities.saturday_mor != "")
        self.assertTrue(test_activities.saturday_aft != "")
        self.assertTrue(test_activities.saturday_eve != "")
        self.assertTrue(test_activities.sunday_mor != "")


"""
Helper Functions for Unit Tests
"""
def build_activity_list():
    ret_list = []
    tuple0 = ('2', '2-Hour Scooter or Segway Rental',
                    'Helmet Rental', 'Scooters South Beach',
                    '1520 Collins Ave #1', 'Miami Beach', 'FL', '33139',
                    65, 'NULL', '305-672-4346', 4.4,
                    'https://scooterssouthbeach.com/',
                    '10:00am', '6:30pm',
                    'TRUE', 'TRUE', 'FALSE', 'FALSE')
    tuple1 = ('3', '2-Hour Electric Bike Rental ',
                    'Helmet Rental', 'Fly E-Bike Miami',
                    '1513 Washington Ave', 'Miami Beach', 'FL', '33139',
                    50, 'NULL', '786-553-5083', 5,
                    'https://www.flyebike.com/miamibeach',
                    '10:00am', '7:00pm',
                    'TRUE', 'TRUE', 'FALSE', 'FALSE')
    tuple2 = ('4', '9 Holes of Golf',
                    'Golf Clubs and Shoe Rental', 'Miami Beach Golf Club',
                    '2301 Alton Road', 'Miami Beach', 'FL', '33140',
                    330, 'NULL', '305-532-3350', 4.6,
                    'https://www.miamibeachgolfclub.com/',
                    '6:30am', '7:30pm',
                    'TRUE', 'TRUE', 'FALSE', 'FALSE')
    tuple3 = ('5', 'Art Museum',
                    'Museum Admission', 'The Wolfsonian',
                    '1001 Washington Ave', 'Miami Beach', 'FL', '33139',
                    0, 'NULL', '305.531.1001', 4.6,
                    'https://wolfsonian.org/',
                    '10:00am', '6:00pm',
                    'TRUE', 'TRUE', 'FALSE', 'TRUE')
    tuple4 = ('6', 'Art Deco District Audio Tour',
                    'Audio Guide for Smart Phone', 'Art Deco Welcome Center',
                    '1001 Ocean Dr', 'Miami Beach', 'FL', '33139',
                    25, 'NULL', '305-763-8026', 3.8,
                    'https://mdpl.org/tours/art-deco-architectural-audio-tour-self-guided/',
                    'NULL', 'NULL',
                    'TRUE', 'TRUE', 'TRUE', 'TRUE')
    ret_list.append(tuple0)
    ret_list.append(tuple1)
    ret_list.append(tuple2)
    ret_list.append(tuple3)
    ret_list.append(tuple4)

    return ret_list


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
