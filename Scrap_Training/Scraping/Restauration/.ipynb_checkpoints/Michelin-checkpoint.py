import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen 
import csv
import os
from tqdm import tqdm
import time


# https://guide.michelin.com/fr/fr/ile-de-france/paris/restaurants/page/2
# https://guide.michelin.com/fr/fr/greater-london/london/restaurants/page/2
# https://guide.michelin.com/fr/fr/berlin-region/berlin/restaurants/page/2
# https://guide.michelin.com/fr/fr/rome-region/rome/restaurants/page/2
# https://guide.michelin.com/fr/fr/madrid-region/madrid/restaurants/page/2
# https://guide.michelin.com/fr/fr/lisboa-region/lisbon/restaurants/page/2
# https://guide.michelin.com/fr/fr/amsterdam-region/amsterdam/restaurants/page/2
# https://guide.michelin.com/fr/fr/brussels-capital-region/brussels/restaurants/page/2
# https://guide.michelin.com/fr/fr/dublin-region/dublin/restaurants/page/2
# https://guide.michelin.com/fr/fr/copenhagen-region/copenhagen/restaurants/page/2

ListeUrl = ["ile-de-france/paris/restaurants/","greater-london/london/restaurants/","berlin-region/berlin/restaurants/","lazio/roma/restaurants/","comunidad-de-madrid/restaurants/","lisboa-region/lisbon/restaurants/","noord-holland/amstelveen/restaurants","bruxelles-capitale/bruxelles/restaurants/","dublin/restaurants/","capital-region/copenhagen/restaurants/","oslo-region/restaurants/","stockholm-region/restaurants/","uusimaa/helsinki/restaurants/","capital-region-iceland/reykjavik/restaurants/","masovia/warsaw/restaurants/","prague/prague/restaurants","central-hungary/budapest/restaurants/","vienna/restaurants/","attica/athens/restaurants/","belgrade-region/restaurants/","zagreb-region/restaurants/",
"skopje-region/skopje/restaurants/","podgorica-region/podgorica/restaurants/","pristina-region/pristina/restaurants/",
"tallinn-region/tallinn/restaurants/","riga-region/riga/restaurants/","vilnius-region/vilnius/restaurants/","chisinau-region/chisinau/restaurants/",
"minsk-region/minsk/restaurants/","kyiv-region/kiev/restaurants/","tbilisi-region/tbilisi/restaurants/","yerevan-region/yerevan/restaurants/",
"baki-region/baku/restaurants/","ankara-region/ankara/restaurants/","nicosia-region/nicosia/restaurants/","valletta-region/valletta/restaurants/",
"vatican-city-region/vatican-city/restaurants/","monaco-region/monaco/restaurants/","san-marino-region/san-marino/restaurants/","andorra-la-vella-region/andorra-la-vella/restaurants/",
"luxembourg-region/luxembourg/restaurants/","vaduz-region/vaduz/restaurants/","bern-region/bern/restaurants/","bratislava-region/bratislava/restaurants/","ljubljana-region/ljubljana/restaurants/",
"zurich-region/zurich/restaurants/","geneve-region/geneva/restaurants/"]

url = "https://guide.michelin.com/fr/fr/"
# la REGION DE MADRID 9 PAGE 
# la region de londres 18 pages
# la region de paris 25 pages  
# la region de berlin 6 pages
# la region de rome 5 pages
# la region de lisbonne 3 pages
# la region d'amsterdam 6 pages
# la region de bruxelles 3 pages
# la region de dublin 2 pages
# la region de copenhague 2 pages
# la region d'oslo 2 pages
# la region de stockholm 2 pages
# la region d'helsinki 2 pages
# la region de reykjavik 1 pages
# la region de varsovie 1 pages
# la region de Prague 2 pages
# Budapest 2
# Vienne 3
# Athènes 2
# Belgrade 1
# Zagreb 1


Data = []
# 22 éléments par pages
url2 = "https://guide.michelin.com/en/restaurants/"+"page/"
print(url2)
for j in tqdm(range(546,835)):  # add 15 later
    if j == 463 or j == 464:
        continue
    url3 = url2 + str(j)
    time.sleep(3)
    print(url3)
    req = Request(url3,headers={'User-agent':'Mozilla/5.0'})
    webpage = urlopen(req)
    page = bs(webpage,"html.parser") # Parser la page


    restaurant_elements = page.findAll('div', class_='card__menu-content card__menu-content--flex js-match-height-content')
    #print(restaurant_elements)
    for Restaurant in restaurant_elements:
        name = Restaurant.findAll('a')
        # Remove the \n in the text
        name[0] = name[0].text.strip()

        # Get the link in the href attribute of the <a> tag
        lien = Restaurant.findAll('a')
        fulllink = 'https://guide.michelin.com' + lien[0]['href']
        #print(fulllink)

        # Get the location of the restaurant
        url5 = fulllink
        print(url5)
        req5 = Request(url5,headers={'User-agent':'Mozilla/4.0'})
        webpage5 = urlopen(req5)
        page5 = bs(webpage5,"html.parser")
        #time.sleep(2)
        # If no address, skip this restaurant

        restaurant_elements5 = page5.findAll('div', class_='col-xl-4 order-xl-8 col-lg-5 order-lg-7 restaurant-details__aside')
        #print(restaurant_elements)

        for elements5 in restaurant_elements5:
            element5 = elements5.findAll('li', class_="restaurant-details__heading--address")
            Address = element5[0].text

        #print(Data)

        # Get the type of restaurant
        Info = page5.findAll('div', class_ = "col-xl-8 col-lg-7 restaurant-details__components")

        for info in Info:
            typeResto = info.findAll('li', class_='restaurant-details__heading-price')
            typeResto[0] = typeResto[0].text.replace('€',"")
            typeResto[0] = typeResto[0].replace('$',"")
            typeResto[0] = typeResto[0].replace('£',"")
            typeResto[0] = typeResto[0].replace('฿',"")
            typeResto[0] = typeResto[0].replace('¥',"")
            typeResto[0] = typeResto[0].replace('₫',"")
            typeResto[0] = typeResto[0].replace('₩',"")
            typeResto[0] = typeResto[0].replace('·',"")
            typeResto[0] = typeResto[0].strip()

        Data.append([name[0],fulllink,typeResto[0],Address])
#print(Data)

    # Number of Data = 50*22*14 = 15400

    # Create a dataframe with the data of Michelin + Yelp
    TempCSV = pd.DataFrame(Data,columns=['Name','Link','Type','Address'])
    TempCSV.to_csv('CSV/TempData.csv',mode='a',index=True,encoding='utf-8')
    print(TempCSV)

df = pd.DataFrame(Data,columns=['Name','Link','Type','Address'])
df.to_csv('CSV/Data.csv',mode='a',index=True,encoding='utf-8')
print(df)
