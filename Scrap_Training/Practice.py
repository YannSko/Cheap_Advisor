import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen 
import csv
import os
import time

 # Parser la page
#Product = page.findAll("div","flex flex-1 flex-col p-3") 
# Permet d'avoir tout les produits ( comics )

for compteur in range(1,56,1) :
    site = 'https://www.lacentrale.fr/listing?makesModelsCommercialNames=&options=&page='+str(compteur)+'&yearMax=1980'
    req = Request(site,headers={'User-agent':'Mozilla/5.0'})
    webpage = urlopen(req)
    page = bs(webpage,"html.parser")
    print(site)
    time.sleep(2)

    for CompteurVoiture in range(1,16,1):
        voiture = page.findAll("a",class_="Vehiculecard_Vehiculecard_vehiculeCard Containers_Containers_containers Containers_Containers_borderRadius Containers_Containers_darkShadowWide")
        nom = voiture[CompteurVoiture].findAll("h2",class_="Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2")
        prix = voiture[CompteurVoiture].findAll("span",class_="Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2")
        AKBC = voiture[CompteurVoiture].findAll("div",class_="Vehiculecard_Vehiculecard_characteristics")
        ModelPrecis = voiture[CompteurVoiture].findAll("div",class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2")


        print('\n')
        print(nom[0].text)
        print(ModelPrecis[0].text)
        print(AKBC[0].text+'')
        print(prix[0].text)

        


