# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 22:14:36 2014

@author: johnnyb
"""

### This is the fucking scraper!!! ###

import requests
from bs4 import BeautifulSoup

# Stránka kterou budeme scrapovat
url = "http://bitstock.cz"

# objekt, který ji představuje
page = requests.get(url)

# tahle proměnná už bude obsahovat samotný html kód stránky
html = page.text

# tady se děje magie, rozparsujeme pomocí Beautifulsoup
# a vrácený objekt uložíme do proměnné soup
soup = BeautifulSoup(html)

for header in soup.find_all('h'):
    print header.text


