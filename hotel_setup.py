
class Hotel:
    def __init__(self,row):
        name, rating, cost = row.split(',')
        self.name = name
        self.rating = rating
        self.cost = cost

def pick_hotel(max_price_pref, min_rating_pref):
    hotel_options = []
    f=open("raw_hotel_info.txt", 'r')
    hotel_string= f.readlines()
    for line in hotel_string:
        #line = line.rstrip()
        obj = Hotel(line)
        if int(obj.rating) >= min_rating_pref:
            if int(obj.cost) <= max_price_pref:
                print(obj.name, "is an optimal pick")
                hotel_options.append(obj.name)            
    print("The following hotels are your options using the current selection:", hotel_options) 
    if hotel_options == []:
        print("No options available at this time")   
    return hotel_options
    f.close()


