#!/usr/bin/env python3
import hotel_setup

def hotel_struct_test():
    try:
        print("Unit Testing Item")
        item = hotel_setup.Hotel("South Beach Plaza Villas,3,86") 
        if item.name == "South Beach Plaza Villas":
            print("Name Success")
        else:
            print("Name Fail", item.name)
        if item.rating == "3":
            print("Rating Success")
        else:
            print("Rating Fail", item.rating)
        if item.cost == "86":
            print("Cost Success!")
        else:
            print("Cost Failure", item.cost)
    except AttributeError as e:
        print("Fail")
        print(e)


def list_test_1():
    max_price_pref = 195
    min_rating_pref = 4
    result =  hotel_setup.pick_hotel(max_price_pref, min_rating_pref)
    if "Gale South Beach" in result:
        if "Iberostar Berkeley Shore" in result:
            print ("Success!")
    else:
        print("fail")

def list_test_2():
    max_price_pref = 50
    min_rating_pref = 1
    result = hotel_setup.pick_hotel(max_price_pref, min_rating_pref)
    if result == []:
        print ("Success!")
    else:
        print("fail")




hotel_struct_test()
list_test_1()
list_test_2()

