#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 22:14:36 2014

@author: johnnyb
"""

### This is the scraper itself, it is a part of the Model ###

import requests
import lxml
from bs4 import BeautifulSoup
import pdb
import json

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

def get_dict(id):
#this is the list of lists
#we are gonna return that afterwards
    sellOrdersList = []

#this represents one sell order
#While iterating through the table we will get this one
# and add it as an item in sellOrdersList
    sellOrderItem = []

    sellbody =  soup.find(id=id)

#sell command for every row, get them all!
#we put them in a so called ResultSet
    sellTableRows = sellbody.find_all('tr')

    sellbodytable = []



# Now we iterate through them, so we get one sell order at a time
    for item in sellTableRows:
        rowlist = {}
        sellTableCells = item.find_all('td')
        row = list(sellTableCells)
        avgprice = float(row[0].text.replace(' ', '').replace(',','.'))
        amount = row[1].text.split('/')
        maxamount = float(amount[0].replace(' ', '').replace(',','.'))
        minamount = float(amount[1].replace(' ', '').replace(',','.'))
        totalprice = float(row[2].text.replace(' ', '').replace(',','.'))
	rowlist['avgprice'] = avgprice
	rowlist['maxamount'] = maxamount
	rowlist['minamount'] = minamount
	rowlist['totalprice'] = totalprice
        sellbodytable.append(rowlist)



#        for cell in sellTableCells:
#            cellValue = float(cell.text)
#             cellValue = cell.text
#             cellValue = cellValue.replace(' ','')
#             cellValue = cellValue.replace(',','')
#             cellValue = float(cellValue)/100

    #get the price from the tdList

#        price=tdList[1]
#        price=price.replace(' ', '')
#        price=price.replace(',', '')
#        price=int(price)/100

    #input("press any key:")

    sbtdict = {} 
    sbtdict['list'] = sellbodytable
    return sbtdict



selldict = get_dict('sellbodyList')
selljson = json.dumps(selldict, indent=3)
with open('sell_orders.json', 'w') as jsonfile:
    jsonfile.write(selljson)

buydict = get_dict('buybodyList')
buyjson = json.dumps(buydict, indent=3)
with open('buy_orders.json', 'w') as jsonfile:
    jsonfile.write(buyjson)


