import os
import geopandas as gpd
from sqlalchemy import create_engine

# 1. Caminho base
base_path = 'data/unidades_consevacao'

# 2. Identifica a pasta mais recente
subpastas = sorted(os.listdir(base_path))
mais_recente = subpastas[-1]  # ex: '2025-03'
caminho_mais_recente = os.path.join(base_path, mais_recente)

# 3. Encontra o arquivo .shp
for arquivo in os.listdir(caminho_mais_recente):
    if arquivo.endswith('.shp'):
        shapefile_path = os.path.join(caminho_mais_recente, arquivo)
        break

# 4. Lê o shapefile com GeoPandas
gdf = gpd.read_file(shapefile_path)

# 5. Conecta ao banco PostgreSQL (com PostGIS)
url = "postgresql://cursoanaliseespacial_user:1tbyyBUZjVqDA5b4S4Rl2HIDot41yUNl@dpg-d0sqf8qdbo4c73fbpemg-a.virginia-postgres.render.com:5432/cursoanaliseespacial"
engine = create_engine(url, connect_args={"sslmode": "require"})

# 6. Salva no banco (PostGIS habilitado)
gdf.to_postgis('unidades_conservacao', engine, if_exists='append', index=False)

print("Shapefile enviado com sucesso ao banco!")
