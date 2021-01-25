# ImmoScraping

ImmoScraping is a Python project using web scraping to create a dataset of Belgian real estate sales data.   

This project was carried out by [Emre Ozan](https://github.com/mremreozan), [Joachim Kotek](https://github.com/jotwo) and [Sara Silvente](https://github.com/silventesa) in Sept 2020 in the context of the course Bouman 2.22 organized by [BeCode](https://github.com/becodeorg), a network of inclusive coding bootcamps.


## Context

Here we used [immoweb real estate company](https://www.immoweb.be/en) and looked for 10000 houses and appartments for sale across Belgium.

Currently, the program grasps the following information (stored in the dataset):
- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No) 
    - If yes: Area
- Garden (Yes/No)
   - If yes: Area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)


## Source code

Source code files correspond to each main project step, and are sequentially ordered: 
1. Get URLs for each property for sale (web automation)
2. Grasp and select target data
3. Store data

### Scraping data from the website

We used Chrome [WebDriver](https://www.selenium.dev/documentation/en/webdriver/) through [Selenium](https://www.selenium.dev/documentation/en/) and [Parsel](https://parsel.readthedocs.io/en/latest/) to get and extract the URL of each result page using XPath selector (the [web_drivers](https://github.com/silventesa/Challenge-collecting-data/tree/master/web_drivers) folder contains also the driver for Firefox).

Our search yielded 333 pages of results. Note that you'll need to change the value below by yours. 

```python
# 1) Obtain URLs through WebDrive

driver = webdriver.Chrome(executable_path='../web_drivers/chromedriver.exe')

# Each URL will be stored in a list.
houses_url = []

# Iterate through all result pages and get the url of each of them. 
# CHANGE 334 VALUE BY YOURS
for i in range(1, 334):
    apikey = str(i)+'&orderBy=relevance'
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page='+apikey
```

We next get the url of each house and store it in a csv file. The same procedure was performed for appartments, since different URLs are used for each kind of property.

### Accessing the information

We got a HTML parsed tree of each property by using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) library.

Data on properties was contained in "windows.classified", under a ''<script>'' tag. 

![HTML_PROPERTY_WINDOW_CLASSIFIED](/screenshots/window_classified_good.png)

We selected this bunch of text and converted it into a python dictionary, where keys = features of properties and values = values (check features dict layout [here](https://github.com/silventesa/Challenge-collecting-data/tree/master/dict)

```python
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
```

We defined `HouseApartmentScraping` class and used class methods to get each property attribute (and store it as a dictionary value) through an iteration performed on the URLs that were previously stored in the csv file.

```python

# Example with number of rooms

    def num_rooms(self):
        try:
            return int(self.house_dict['property']['bedroomCount'])
        except:
            return None
```

Store values into a `defaultdict()`

```python
houses_apartments_dict = defaultdict(list)

with open('../csv_files/houses_apartments_urls.csv', 'r') as file:
    url = file.readline()
    while url != "":
        
        houses_class = HouseApartmentScraping(url)
        
        houses_apartments_dict['Locality'].append(houses_class.locality)
        houses_apartments_dict['Type of property'].append(houses_class.type_property)
        houses_apartments_dict['Subtype of property'].append(houses_class.subtype)
        houses_apartments_dict['Price'].append(houses_class.price)
        
        ...
```


### Store data

We finally converted our dict into a pandas DataFrame and saved it as a csv.
