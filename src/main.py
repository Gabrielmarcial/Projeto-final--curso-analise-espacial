from load import load_shape
from extract import extrac_load_queimadas

# EXTRACT

extrac_load_queimadas()

# LOAD


load_shape('data/quilombos/2025-08/Quilombos-SAB-INCRA.shp','quilombos')

load_shape('data/unidades_consevacao/2025-03/cnuc_2025_03.shp','unidades_conservacao')

load_shape('data/terra_indigina/2025-08/tis_poligonaisPolygon.shp','terra_indigina')



# TRANSFORM