import os
import pandas as pd
from sqlalchemy import create_engine
from ..utils import URL_DB

# 1. Caminho base
base_path = 'data/queimadas'
print(URL_DB)
# 2. Lista as subpastas e pega a mais recente
subpastas = sorted(os.listdir(base_path))
mais_recente = subpastas[-1]  # Ex: '2025-07'
caminho_mais_recente = os.path.join(base_path, mais_recente)

# 3. Lê todos os CSVs da pasta mais recente
csvs = [
    pd.read_csv(os.path.join(caminho_mais_recente, arquivo))
    for arquivo in os.listdir(caminho_mais_recente)
    if arquivo.endswith('.csv')
]

# 4. Junta tudo em um único DataFrame
df = pd.concat(csvs, ignore_index=True)

# 5. Conecta ao banco PostgreSQL (ajuste com suas credenciais)
url = "postgresql://cursoanaliseespacial_user:1tbyyBUZjVqDA5b4S4Rl2HIDot41yUNl@dpg-d0sqf8qdbo4c73fbpemg-a.virginia-postgres.render.com:5432/cursoanaliseespacial"
engine = create_engine(url, connect_args={"sslmode": "require"})

# 6. Salva no banco (append = adiciona sem apagar dados anteriores)
df.to_sql('queimadas_mensal', engine, if_exists='append', index=False)

print("Dados inseridos com sucesso.")
