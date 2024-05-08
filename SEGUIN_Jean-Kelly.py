# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:23:04 2022

@author: SGJ2994A
"""
# importation des bilbiothèques
import os
import geopandas as gpd
import pandas as pd
import rasterio
from rasterstats import zonal_stats

# chemin vers le fichiers

path="D:/Programmation/Projet_raster/"

os.chdir(path) # changement d'environnement de Travail

# lectures des fichiers raster et vecteur

raster=rasterio.open("zip://D:/Programmation/Projet_raster/projets.zip!/FUSION_DEC_2154.tif")

vecteurs=gpd.read_file("zip://D:/Programmation/Projet_raster/projets.zip!/couches_projets.shp")

# chemin vers raster et vecteurs dans le zip 

tif="zip://D:/Programmation/Projet_raster/projets.zip!/FUSION_DEC_2154.tif"
vec="zip://D:/Programmation/Projet_raster/projets.zip!/couches_projets.shp"
 
# verification des crs avec une condition pour reprojetter la couche si jamais les crs ne sont pas identiques

if raster.crs == vecteurs.crs.srs :
    print("crs bon!")
else : vecteurs.to_crs(epsg=2154)

# création d'une fonction permettant d'extraire la valeur moyenne contenu dans un polygone
# ou un point et sortir en csv en conservant que les colonnes id et mean (moyenne)

def mean_csv():
    
    # moyenne par zone en geojson en spécifiant le numéro de la bande parce qu'il 
    # y a plusieurs bandes et une bande = une date
    
    geojson=zonal_stats(vec, 
                     tif, band=1,
                geojson_out=True,
                stats="mean")
    
    
    # on crée un dataframe à partir du geojson
    json = gpd.GeoDataFrame.from_features(geojson)

    # geojson en csv avec les colonnes id(index), id_lot et mean(moyennes)

    json[{'ID_ILOT','mean'}].to_csv('test.csv', index=True)

# on teste la fonction 
mean_csv()


# on ouvre fichier csv
csv=pd.read_csv('test.csv')


    



