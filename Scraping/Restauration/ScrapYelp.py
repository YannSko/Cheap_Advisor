import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen 
import csv
import os
import time


url = "https://www.yelp.com/search?find_desc=restaurant&find_loc=Berlin%2C+Germany&sortby=review_count"
end_url = "&start="
for i in range (0,100,10):
    url = url + end_url + str(i)
    
    req = Request(url,headers={'User-agent':'Mozilla/5.0'})
    webpage = urlopen(req)
    page = bs(webpage,"html.parser") # Parser la page
    restaurant_elements = page.findAll('div', class_='arrange__09f24__LDfbs css-1qn0b6x')
    print(restaurant_elements)
    for restaurant in restaurant_elements:
    # Nom du restaurant
        name = restaurant.find('a', class_='link__09f24__1kwXV').text
        print(name)