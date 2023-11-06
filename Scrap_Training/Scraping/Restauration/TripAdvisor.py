import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen 
import csv
import os
from tqdm import tqdm
import time


for i in tqdm(range(30,10000,30)):
    url = "https://www.tripadvisor.fr/Restaurants-g187147-oa"+str(i)+"-Paris_Ile_de_France.html"
    time.sleep(3)
    print(url)
    req = Request(url,headers={'User-agent':'Mozilla/5.0'})
    webpage = urlopen(req)
    page = bs(webpage,"html.parser") # Parser la page
    restaurant_elements = page.findAll('div', class_='Ikpld f e')
    # Cherche tout les url dans restaurant elements
    print("help")
    #print(restaurant_elements)
    for element in restaurant_elements:
        AllTitre = element.findAll('div',class_='vIjFZ Gi o VOEhq')
        for Titre in AllTitre:
            Titre = Titre.text  
            print(Titre)
