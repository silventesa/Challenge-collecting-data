# ImmoScraping

## What is this?

A python program using web scraping to create a dataset of Belgian real estate sales data.   

### Where does it come from?

This project was carried out in Sept 2020 in the context of the course Bouman 2.22 organized by [BeCode](https://github.com/becodeorg), a network of inclusive coding bootcamps.

### Who's there?

Three learners and collaborators, [Emre Ozan](https://github.com/mremreozan), [Joachim Kotek](https://github.com/jotwo) and [Sara Silvente](https://github.com/silventesa), designed the program.


## Let's go through it!

The [immoweb](https://github.com/mremreozan/immoweb_scraping/blob/master/immoweb.ipynb) jupyter file provides the ways to scrap data from the results of a search in a real estate company website and store it in a csv file.

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


### Scraping data from the website

The first step is to get the url of each page of results by using **webdriver** and **selector**, from **selenium** and **parsel** libraries. 
Each page of the search results contains a number of links to houses for sale (here, around 30). For example, our search in immoweb yielded 333 pages of results. Note that you'll need to change the value below by yours. 

![FIRST_CELL_ITERATING_RESULTS_PAGESURLS](/screenshots/sc1.png)

We next get the url of each house to a csv file and repeat the same procedure with a search made on appartments, since they have a different url from the one of houses. You can skip this step if you use a website in which all results are contained in the same url. 

#### Accessing the information

We get a the HTML parsed tree of each property by using the python **Beautiful Soup** package.

As you can see below, propertys' data is stored _in the form of_ a python dictionary, and it _seems_ to be assigned to a variable called "window.classified" under a ``<script>`` tag with the attributes ``type="text/javascript"``. 

![HTML_PROPERTY_WINDOW_CLASSIFIED](/screenshots/window_classified_good.png)

We use the string "window.classified" as a reference to select the part we are interested in, and then create a proper python dictionary by which property's attributes are treated as keys and values as values.

![CREATION_DICTIONAY](/screenshots/dictionary.png)

The dictionary as well as the entries for each property attribute are defined created by means of an instance methods in the **class `HouseApartmentScraping`**. 

We iterate through all the urls that have been previously stored in the csv file and we store the values for each property attribute in a ``defaultdict``.

![COLLECT_DEFAULTDICT](/screenshots/collect_defaultdict.png)

#### Store the data in a csv file

Finally, we store our results in a csv file by using **pandas dataframe**, which you can also use to visualize the data. And voilà!

![FINAL_CSV_PANDAS](/screenshots/store_csv_pandas.png)


### Features Dict Layout

house_dict = {
<br />&nbsp;    "flags":{
        "isPublicSale": <class 'bool'>,
        "isNotarySale": <class 'bool'>,
        "isAnInteractiveSale": <class 'bool'>
    },
    "property": {
        "location": {
            "postalCode": <class 'str'>,
        },
        "building": {
            "condition": <class 'str'>,
            "facadeCount": <class 'int'>
        },
        "land": {
            "surface": <class 'int'>
        },
        "kitchen": {
            "type": <class 'str'>
        },
        "type": <class 'str'>,
        "subtype": <class 'str'>,
        "netHabitableSurface": <class 'int'>,
        "bedroomCount": <class 'int'>,
        "hasGarden": <class 'bool'>,
        "gardenSurface": <class 'int'>,
        "hasTerrace": <class 'bool'>,
        "terraceSurface": <class 'int'>,
        "fireplaceExists": <class 'bool'>,
        "hasSwimmingPool": <class 'bool'>
    },
    "transaction": {
        "sale": { 
            "price": <class 'int'>,
            "isFurnished": <class 'bool'>
        }
    }
}
