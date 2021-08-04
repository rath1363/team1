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


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
