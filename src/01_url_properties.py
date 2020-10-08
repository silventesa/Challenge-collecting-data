# to extract all properties urls (needed to handle with javascript)
from selenium import webdriver 

# to access the html content of a single property url
import requests 

# to select parts of an XML or HTML text using CSS or XPath and extract data from it
from parsel import Selector 


# 1) Obtain 10000 url of houses with webdriver (appartments below)

driver = webdriver.Chrome(executable_path='../web_drivers/chromedriver.exe')

# The url of each house that resulted from the search will be stored in the "houses_url" list.
houses_url = []

# Iterate through all result pages (i) and get the url of each of them
for i in range(1, 334):
    apikey = str(i)+'&orderBy=relevance'
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page='+apikey

    # An implicit wait tells WebDriver to poll the DOM for a
    #  certain amount of time when trying to find any element 
    #     (or elements) not immediately available. 
    driver.implicitly_wait(10)
    
    # The first thing you’ll want to do with WebDriver is navigate
    #   to a link. The normal way to do this is by calling get method:    
    driver.get(url)

    # Selector allows you to select parts of an XML or HTML text using CSS
    #   or XPath expressions and extract data from it.
    sel = Selector(text=driver.page_source) 

    # Store the xpath query of houses
    xpath_houses = '//*[@id="main-content"]/li//h2//a/@href'
    
    # Find nodes matching the xpath ``query`` and return the result
    page_houses_url = sel.xpath(xpath_houses).extract()
    
    # There are approximately 30 houses in each page.
    # Add each page url list to houses_url, like in a matrix.
    houses_url.append(page_houses_url)

# Store all houses urls in a csv file
with open('../csv_files/houses_apartments_urls.csv', 'w') as file:
    for page_url in houses_url:
        for url in page_url:
            file.write(url+'\n')

# The url of each appartment that resulted from the search will be stored in the "houses_url" list
apartments_url = []

for i in range(1, 334):
    # We used 'i' to build urls of the 333 page in immoweb.
    #   So, we can reach 333 pages with for loop.
    apikey = str(i)+'&orderBy=relevance'
    url = 'https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page='+apikey

    # An implicit wait tells WebDriver to poll the DOM for a
    #   certain amount of time when trying to find any element 
    #     (or elements) not immediately available. 
    driver.implicitly_wait(10)
    
    # The first thing you’ll want to do with WebDriver is navigate
    #   to a link. The normal way to do this is by calling get method:    
    driver.get(url)

    # Selector` allows you to select parts of an XML or HTML text using CSS
    #   or XPath expressions and extract data from it.
    sel = Selector(text=driver.page_source) 

    # xpath query of the houses in the immoweb page
    xpath_apartments = '//*[@id="main-content"]/li//h2//a/@href'
    
    # Find nodes matching the xpath ``query`` and return the result
    page_apartments_url = sel.xpath(xpath_apartments).extract()
    
    # There are approximately 30 houses in each page.
    # We add each page url list to houses_url like matrix.
    apartments_url.append(page_apartments_url)

# As with houses, store all appartments urls in the same csv file
with open('../csv_files/houses_apartments_urls.csv', 'a') as file:
    for page_url in apartments_url:
        for url in page_url:
            file.write(url+'\n')