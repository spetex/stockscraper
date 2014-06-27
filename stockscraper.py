# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 22:14:36 2014

@author: johnnyb
"""

### This is the mighty scraper!!! ###

import requests
import lxml
from bs4 import BeautifulSoup

# Site we want to scrape
url = "http://bitstock.cz"

# to object
page = requests.get(url)

# this object becomes the code of the page
html = page.text

# magic, parse html with beatifulsoup to get a sort of a dictionary object
# now using a lxml parser module
soup = BeautifulSoup(html, "lxml")

# go trough the table with sell commands by id
sellbody =  soup.find(id="sellbodyList")

#sell command for every row, get them all!
sellTableRows = sellbody.find_all('tr')

 
     
    


