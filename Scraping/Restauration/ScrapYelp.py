import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen 
import csv
import os
from tqdm import tqdm
import time


Liste_Nom = []
Liste_Lien = []
Data = []





Europe_Capital = ["Berlin","Paris","Rome","Madrid","London","Lisbon","Amsterdam","Brussels","Dublin","Copenhagen","Oslo","Stockholm","Helsinki","Reykjavik","Moscow","Warsaw","Prague","Budapest","Vienna","Athens","Bucharest","Sofia","Belgrade","Zagreb","Tirana","Skopje","Podgorica","Pristina","Tallinn","Riga","Vilnius","Chisinau","Minsk","Kiev","Tbilisi","Yerevan","Baku","Ankara","Nicosia","Valletta","Vatican City","Monaco","San Marino","Andorra la Vella","Luxembourg","Vaduz","Bern","Bratislava","Ljubljana","Zurich","Geneva","Prague","Budapest","Vienna","Athens","Bucharest","Sofia","Belgrade","Zagreb","Tirana","Skopje","Podgorica","Pristina","Tallinn","Riga","Vilnius","Chisinau","Minsk","Kiev","Tbilisi","Yerevan","Baku","Ankara","Nicosia","Valletta","Vatican City","Monaco","San Marino","Andorra la Vella","Luxembourg","Vaduz","Bern","Bratislava","Ljubljana","Zurich","Geneva"]
for i in range (0,len(Europe_Capital),1):
    for j in tqdm(range(0,200,10)):
        time.sleep(3)
        url = "https://www.yelp.com/search?find_desc=restaurant&find_loc="+Europe_Capital[i]+"&sortby=review_count&start=" + str(j)
        print(url)
        req = Request(url,headers={'User-agent':'Mozilla/5.0'})
        webpage = urlopen(req)
        page = bs(webpage,"html.parser") # Parser la page
        restaurant_elements = page.findAll('div', class_='css-ady4rt')
        #print(restaurant_elements)
        for restaurant in restaurant_elements:
        # Nom du restaurant
            name = restaurant.findAll('a', class_='css-19v1rkv')
            #print(name[0].text)
            Liste_Nom.append(name[0].text)

            # Get the link in the href attribute of the <a> tag
            lien = restaurant.findAll('a', class_='css-19v1rkv')
            fulllink = 'https://www.yelp.com' + lien[0]['href']
            #print(fulllink)
            Liste_Lien.append(fulllink)

            # Get the location of the restaurant

            url = fulllink
            req = Request(url,headers={'User-agent':'Mozilla/5.0'})
            webpage = urlopen(req)
            page = bs(webpage,"html.parser")
            time.sleep(3)
            # If no address, skip this restaurant

            restaurant_elements = page.findAll('p', class_='css-qyp8bo')
            #print(restaurant_elements[0].text)
            if restaurant_elements:
                Address = restaurant_elements[0].text
            else:
                Address = "No address"





            # Get the type of restaurant
            type = restaurant.findAll('span', class_='css-1d8srnw')
            for RestoType in type:
                Temp = 0
                
                TypeName = RestoType.findAll('span', class_='css-11bijt4') 
                #print(TypeName)

                #Remove empty list 
                if TypeName:
                    Temp = 1
                    # Doit ajouté le deuxieme type de restaurant s'il existe
                if len(TypeName) > 1:
                    Temp = 2
                if Temp == 2:
                    TypeResto = TypeName[0].text +" - "+ TypeName[1].text
                elif Temp == 1:
                    TypeResto = name[0].text,fulllink,TypeName[0].text



            Data.append([name[0].text,fulllink,TypeResto,Address])

            #print(Data)
            #print('\n')
print(Data)
