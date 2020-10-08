# impot HouseApartmentScraping class
from collecting_data_from_url_properties import HouseApartmentScraping 

# to build a defaultdict
from collections import defaultdict

# to build the dataframe
import pandas as pd 

# 3) store all data of properties into a defaultdict
houses_apartments_dict = defaultdict(list)

with open('../csv_files/houses_apartments_urls.csv', 'r') as file:
    url = file.readline()
    while url != "":
        
        houses_class = HouseApartmentScraping(url)
        
        houses_apartments_dict['Locality'].append(houses_class.locality)
        houses_apartments_dict['Type of property'].append(houses_class.type_property)
        houses_apartments_dict['Subtype of property'].append(houses_class.subtype)
        houses_apartments_dict['Price'].append(houses_class.price)
        houses_apartments_dict['Type of sale'].append(houses_class.type_sale)
        houses_apartments_dict['Number of rooms'].append(houses_class.num_rooms)
        houses_apartments_dict['Living surface area'].append(houses_class.area)
        houses_apartments_dict['Kitchen'].append(houses_class.kitchen)
        houses_apartments_dict['Furnished'].append(houses_class.furnished)
        houses_apartments_dict['Open fire'].append(houses_class.fire)
        houses_apartments_dict['Terrace'].append(houses_class.terrace_area)
        houses_apartments_dict['Garden'].append(houses_class.garden_area)
        houses_apartments_dict['Surface of the land'].append(houses_class.land)
        houses_apartments_dict['Number of facades'].append(houses_class.num_facade)
        houses_apartments_dict['Swimming pool'].append(houses_class.pool)
        houses_apartments_dict['State of the building'].append(houses_class.state)

        url = file.readline()

# 3) We store all data to a csv file with dataframe.
df = pd.DataFrame(houses_apartments_dict)
df.to_csv('../csv_files/all_data_of_the_houses.csv')