import pandas as pd
from sqlalchemy import create_engine 
from dotenv import load_dotenv
import os
import geopandas as gpd

load_dotenv()

URL_DB = os.getenv('URL_DB') 
engine = create_engine(URL_DB)



def load_shape(shapefile,name):
    gdf = gpd.read_file(shapefile,encoding='latin1')
    gdf.to_postgis(name,engine, schema='raw', if_exists='append', index=False)
    print('Shapefile salvo no banco !!')