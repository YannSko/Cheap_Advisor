import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen 
import csv
import os
import time


site = ''
req = Request(site,headers={'User-agent':'Mozilla/5.0'})
webpage = urlopen(req)
page = bs(webpage,"html.parser") # Parser la page
#Product = page.findAll("div","flex flex-1 flex-col p-3") 
# Permet d'avoir tout les produits ( comics )

data = [] # création d'une liste qui va contenir nos data
alldata = []
test = page.findAll("","")