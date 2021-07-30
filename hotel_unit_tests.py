#!/usr/bin/env python3
import hotel_setup
import unittest


class hotelTest(unittest.TestCase):

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
        max_cost_pref = 250
        min_rating_pref = 3
        dbname = 'lodging_test'
        item_1 = hotel_setup.Hotel(dbname, max_cost_pref, min_rating_pref) 
        self.assertEqual(item_1.name, "N/A", "Error in attribute: name" )
        self.assertEqual(item_1.rating, 0, "Error in attribute: rating" )
        self.assertEqual(item_1.rating_pref, min_rating_pref, "Error in attribute: rating_pref" )
        self.assertEqual(item_1.cost, 0, "Error in attribute: cost" )
        self.assertEqual(item_1.cost_pref, max_cost_pref, "Error in attribute: cost_pref" )
        self.assertEqual(item_1.address, "N/A", "Error in attribute: address")
        self.assertEqual(item_1.phone, 0, "Error in attribute: phone")
        self.assertEqual(item_1.database, 'lodging_test', "Error in attribute: database")


    def test_init_cost(self):
        min_rating_pref = 3
        str_cost = "hello"
        flt_cost = 314.15
        dbname = 'lodging_test'

        with self.assertRaises(TypeError) as e:
            hotel_setup.Hotel(dbname, str_cost, min_rating_pref) 
        with self.assertRaises(TypeError) as e:
            hotel_setup.Hotel(dbname, flt_cost, min_rating_pref)

    def test_init_rating(self):
        max_cost_pref = 300
        str_rating = "hello"
        flt_rating = 314.15
        high_rating = 6
        dbname = 'lodging_test'

        with self.assertRaises(TypeError) as e:
            hotel_setup.Hotel(dbname, max_cost_pref, str_rating) 
        with self.assertRaises(TypeError) as e:
            hotel_setup.Hotel(dbname, max_cost_pref, flt_rating)
        with self.assertRaises(Exception) as e:
            hotel_setup.Hotel(dbname, max_cost_pref, high_rating)

    def test_db_input(self):
        max_cost_pref = 300
        min_rating_pref = 3
        int_db = 999
        flt_db = 99.99

        with self.assertRaises(TypeError) as e:
            hotel_setup.Hotel(int_db, max_cost_pref, min_rating_pref) 
        with self.assertRaises(TypeError) as e:
            hotel_setup.Hotel(flt_db, max_cost_pref, min_rating_pref)

    def test_pick_hotel(self):
        max_cost_pref_1 = 250
        min_rating_pref_1 = 4
        dbname = 'lodging_test'
        item_1 = hotel_setup.Hotel(dbname, max_cost_pref_1, min_rating_pref_1)
        item_1.pick_hotel()
        self.assertTrue(item_1.name == "Best Hotel")
        self.assertTrue(item_1.rating == 5)
        self.assertTrue(item_1.cost == 200)
        self.assertTrue(item_1.address == "102 abc Ave, Miami Beach, FL 33139")
        self.assertTrue(item_1.phone == 2222222222)

        max_cost_pref_2 = 49
        min_rating_pref_2 = 1
        item_2 = hotel_setup.Hotel(dbname, max_cost_pref_2, min_rating_pref_2)
        item_2.pick_hotel
        self.assertTrue(item_2.name == "N/A")
        self.assertTrue(item_2.rating == 0)
        self.assertTrue(item_2.cost == 0)
        self.assertTrue(item_2.address == "N/A")
        self.assertTrue(item_2.phone == 0)



if __name__ == '__main__':
    unittest.main()

