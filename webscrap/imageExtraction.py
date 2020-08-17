# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:17:11 2020

@author: Kogoon
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:09:52 2020

@author: Kogoon
"""
import requests
from bs4 import BeautifulSoup

url  = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

first_img = soup.find(name='img')
print(first_img)
print("\n")

target_img = soup.find(name='img', attrs={'alt':'Seoul-Metro-2004-20070722.jpg'})
print(target_img)
