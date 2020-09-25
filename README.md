# Title

## What is this?

A python program using web scraping to create a dataset of Belgian real estate sales data.   

### Where does it come from?

This project was carried out in Sept 2020 in the context of the course Bouman 2.22 organized by [BeCode](https://github.com/becodeorg), a network of inclusive coding bootcamps.

### Who's there?

Three learners and collaborators, [Emre Ozan](https://github.com/mremreozan), [Joachim Kotek](https://github.com/jotwo) and [Sara Silvente](https://github.com/silventesa), designed the program.


## Let's go through it!

The [immoweb](https://github.com/mremreozan/immoweb_scraping/blob/master/immoweb.ipynb) file provides the ways to: 
1. scrap data from the results of a search in a real estate company website
2. store the data in a csv file

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


### 1. Scraping data from the website
