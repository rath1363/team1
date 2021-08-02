#!/usr/bin/env python3
import restaurant_setup
import unittest


class restaurantTest(unittest.TestCase):

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

    def test_init(self):
        min_cost_pref_dollars = 1
        max_cost_pref_dollars = 600
        dbname = 'restaurant_test'
        item_1 = restaurant_setup.Restaurant(dbname, min_cost_pref_dollars, max_cost_pref_dollars) 
        self.assertEqual(item_1.name, "N/A", "Error in attribute: name" )
        self.assertEqual(item_1.cost, 0, "Error in attribute: cost" )
        self.assertEqual(item_1.min_cost_pref_dollars, min_cost_pref_dollars, "Error in attribute: min_cost_pref" )
        self.assertEqual(item_1.max_cost_pref_dollars, max_cost_pref_dollars, "Error in attribute: max_cost_pref" )       
        self.assertEqual(item_1.address, "N/A", "Error in attribute: address")
        self.assertEqual(item_1.phone, 0, "Error in attribute: phone")
        self.assertEqual(item_1.database, 'restaurant_test', "Error in attribute: database")


    def test_init_cost(self):
        str_cost = "hello"
        flt_cost = 314.15
        ok_cost = 30
        high_cost = 500
        low_cost = 0
        dbname = 'restaurant_test'

        with self.assertRaises(TypeError) as e:
            restaurant_setup.Restaurant(dbname, str_cost, ok_cost) 
        with self.assertRaises(TypeError) as e:
            restaurant_setup.Restaurant(dbname, flt_cost, ok_cost)
        with self.assertRaises(TypeError) as e:
            restaurant_setup.Restaurant(dbname, ok_cost, str_cost) 
        with self.assertRaises(TypeError) as e:
            restaurant_setup.Restaurant(dbname, ok_cost, flt_cost)    
        with self.assertRaises(Exception) as e:
            restaurant_setup.Restaurant(dbname, low_cost, low_cost)
        with self.assertRaises(Exception) as e:
            restaurant_setup.Restaurant(dbname, high_cost, ok_cost)


    def test_db_input(self):
        min_cost_pref = 20
        max_cost_pref = 30
        int_db = 999
        flt_db = 99.99

        with self.assertRaises(TypeError) as e:
            restaurant_setup.Restaurant(int_db, min_cost_pref, max_cost_pref) 
        with self.assertRaises(TypeError) as e:
            restaurant_setup.Restaurant(flt_db, min_cost_pref, max_cost_pref)

    def test_dollar_conversion_helper(self):
        cost_1 = 1
        cost_2 = 11
        cost_3 = 26
        cost_4 = 50
        dbname = 'restaurant_test'
        
        item_1= restaurant_setup.Restaurant(dbname, cost_1, cost_2)
        self.assertTrue(item_1.min_cost_pref == 1)
        self.assertTrue(item_1.max_cost_pref == 2)
        item_2= restaurant_setup.Restaurant(dbname, cost_3, cost_4)
        self.assertTrue(item_2.min_cost_pref == 3)
        self.assertTrue(item_2.max_cost_pref == 4)
    

    def test_pick_Restaurant(self):
        min_cost_pref_1 = 50
        max_cost_pref_1 = 600
        dbname = 'restaurant_test'
        item_1 = restaurant_setup.Restaurant(dbname, min_cost_pref_1, max_cost_pref_1)
        item_1.pick_restaurant()
        self.assertTrue(item_1.name == "Burger King")
        self.assertTrue(item_1.cost == 4)
        self.assertTrue(item_1.address == "102 abc Ave, Miami Beach, FL 33139")
        self.assertTrue(item_1.phone == 2222222222)
        
        min_cost_pref_2 = 27
        max_cost_pref_2 = 28
        item_2 = restaurant_setup.Restaurant(dbname, min_cost_pref_2, max_cost_pref_2)
        item_2.pick_restaurant()
        self.assertTrue(item_2.name == "N/A")
        self.assertTrue(item_2.cost == 0)
        self.assertTrue(item_2.address == "N/A")
        self.assertTrue(item_2.phone == 0)



if __name__ == '__main__':
    unittest.main()


