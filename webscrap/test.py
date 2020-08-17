# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:30:49 2020

@author: Kogoon

import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=N7mZsC_4cmE"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

comment_list = soup.select('#content-text')

print(comment_list)

#fail
"""
from selenium import webdriver as wd
driver = wd.Chrome(executable_path="chromedriver.exe")
url = "https://www.naver.com"
driver.get(url)

# install driver necessary
