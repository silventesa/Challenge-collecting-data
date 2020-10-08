# to access the html content of a single property url
import requests 

# to select parts of an XML or HTML using BeautifulSoup (XPath not supported)
from bs4 import BeautifulSoup 

# to use regular expressions
import re 

# to build a dictionary form a string
import json 
 
class HouseApartmentScraping:
    '''
    Define a class through which properties' data will be scraped

    Each url represents a property (house or appartment), 
    each of which has a number of attributes (e.g., locality, type_property etc.). 
    We thus create a class defining the attributes of each property

    :param url: urls of properties in houses_apartments_urls.csv
    :param html: html code of urls
    :param soup: BeautifulSoup text of htmls
    :param house_dict: attribute referring to the set of houses data 
        (stored in a dictionary; see below in house dict method)
    '''
    def __init__(self, url):
        self.url = url
        
        # attributes to obtain html code (self.html) and select parts of it (self.soup)
        self.html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.html,'html.parser')
        
        # attribute referring to the set of houses data (stored in a dictionary; see below)
        self.house_dict = self.house_dict()
        
        # set of attributes collected in the dictionary
        self.type_property = self.type_property()
        self.locality = self.locality()
        self.subtype = self.subtype()
        self.price = self.price()
        self.type_sale = self.type_sale()
        self.num_rooms = self.num_rooms()
        self.area = self.area()
        self.kitchen = self.kitchen()
        self.furnished = self.furnished()
        self.fire = self.fire()
        self.terrace_area = self.terrace_area()
        self.garden_area = self.garden_area()
        self.land = self.land()
        self.num_facade = self.num_facade()
        self.pool = self.pool()
        self.state = self.state()
        
        
    def house_dict(self):
        '''
        Define a method that creates the dictionary with attributes as keys and houses' values as values
        '''
        try:
            # The relevant info is under a "script" tag in the website
            result_set = self.soup.find_all('script',attrs={"type" :"text/javascript"})
            
            # Iterate through the "script" tags found and keep the one containing the substring "window.classified"
            # which contains all the relevant info
            for tag in result_set:
                if 'window.classified' in str(tag.string):
                    window_classified = tag
                    #when we've found the right tag we can stop the loop earlier
            
            
            # Access to the string attribute of the tag and remove leading and trailing whitespaces (strip)break
            wcs = window_classified.string
            wcs.strip()
            
            # Keep only the part of the string that will be converted into a dictionary
            wcs = wcs[wcs.find("{"):wcs.rfind("}")+1]
            
            # Convert it into a dictionary through json library
            house_dict = json.loads(wcs)
            return house_dict
        except:
            return None

    # Define a method to scrap each property attribute
    def type_property(self):
        try:
            return self.house_dict['property']['type']
        except:
            return None        
    
    def locality(self):
        try:
            return self.house_dict['property']['location']['postalCode']
        except:
            return None
    
    def subtype(self):
        try:
            return self.house_dict['property']['subtype']
        except:
            return None
    
    def price(self):
        try:
            return int(self.house_dict['transaction']['sale']['price'])
        except:
            return None
    
    def type_sale(self):
        try:
            if self.house_dict['flags']['isPublicSale'] == True:
                return 'Public Sale'
            elif self.house_dict['flags']['isNotarySale'] == True:
                return 'Notary Sale'
            elif self.house_dict['flags']['isAnInteractiveSale'] == True:
                return 'Intractive Sale'
            else:
                return None
        except:
            return None 
    
    def num_rooms(self):
        try:
            return int(self.house_dict['property']['bedroomCount'])
        except:
            return None
    
    def area(self):
        try:
            return int(self.house_dict['property']['netHabitableSurface'])
        except:
            return None
    
    def kitchen(self):
        try: 
            kitchen_type = self.house_dict['property']['kitchen']['type']
            if kitchen_type:
                return 1
            else:
                return 0        
        except:
            return None
        
    def furnished(self):
        try:
            furnished = self.house_dict['transaction']['sale']['isFurnished']
            if furnished == True:
                return 1
            else:
                return 0
            
        except:
            return None
    
    def fire(self):
        try:
            fire = self.house_dict['property']['fireplaceExists']
            if fire == True:
                return 1 
            else:
                return 0                
        except:
            return None
    
    def terrace_area(self):
        try:
            if self.house_dict['property']['hasTerrace'] == True:
                return int(self.house_dict['property']['terraceSurface'])
            else:
                return 0
        except:
            return None
    
    def garden_area(self):
        try:
            if self.house_dict['property']['hasGarden'] ==  True:
                return self.house_dict['property']['gardenSurface']
            else:
                return 0
        except:
            return None
    
    def land(self):
        try:
            if self.house_dict['property']['land'] != None:
                return self.house_dict['property']['land']['surface']
            else:
                return 0
        except:
            return None
        
    def num_facade(self):
        try:
            return int(self.house_dict['property']['building']['facadeCount'])
        except:
            return None
        
    def pool(self):
        try: 
            swim_regex = re.findall('swimming pool', str(self.html))
            if swim_regex:
                return 1
            else:
                return 0
        except:
            return None
        
    def state(self): 
        try:
            return self.house_dict['property']['building']['condition']
        except:
            return None