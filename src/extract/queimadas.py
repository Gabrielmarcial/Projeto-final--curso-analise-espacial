import requests
import os

url = "https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/mensal/Brasil/focos_mensal_br_202402.csv"


output_dir = "data"

filename = os.path.basename(url)
print(filename)
output_path = os.path.join(output_dir, filename)


response = requests.get(url)

with open(output_path, "wb") as f:
    f.write(response.content)
