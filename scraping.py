#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:01:04 2018

@author: tcake
"""

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://mappinggm.org.uk/gmodin/?lyrs=baseline_housing_land_supply#os_maps_light/11/53.5069/-2.3201"
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser' )
print(page_soup.h1)