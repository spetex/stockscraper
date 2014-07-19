# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 22:14:36 2014

@author: johnnyb
"""

### This is the scraper itself, it is a part of the Model ###

import requests
import lxml
from bs4 import BeautifulSoup

# Site we want to scrape
url = "http://bitstock.cz/en"

# to object
page = requests.get(url)

# this object becomes the code of the page
html = page.text

# magic, parse html with beatifulsoup to get a sort of a dictionary object
# now using a lxml parser module
soup = BeautifulSoup(html, "lxml")




# From now on, we just scrape the Sell orders
# whole body of the relevant table has id sellbodyList
#get that

def getSellList():
#this is the list of lists
#we are gonna return that afterwards
    sellOrdersList = []

#this represents one sell order
#While iterating through the table we will get this one
# and add it as an item in sellOrdersList
    sellOrderItem = []

    sellbody =  soup.find(id="sellbodyList")

#sell command for every row, get them all!
#we put them in a so called ResultSet
    sellTableRows = sellbody.find_all('tr')


# Now we iterate through them, so we get one sell order at a time
    for td in sellTableRows:
        print("item info: 1")
        tdString = td.text
        print tdString
        tdList = tdString.split("\n")
        print tdList
    
    #get the price from the tdList
    
        price=tdList[1]
        price=price.replace(' ', '')
        price=price.replace(',', '')
        price=int(price)/100
    
    #input("press any key:")
        break
    
    return getSellList

        

 
     
    


