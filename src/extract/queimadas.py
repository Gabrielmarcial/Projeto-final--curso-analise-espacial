import requests
import os
import pandas as pd


today = pd.Timestamp.today()
end_date = today.strftime('%Y-%m')


url_base = "https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/mensal/Brasil/"

output_dir = f"data/queimadas/{end_date}"
os.makedirs(output_dir,exist_ok=True)


df_control = pd.read_csv('data/control/controle_mensal_queimadas.csv') 
star_date = df_control['ano_mes'].to_list()[0]

datas = pd.date_range(start=star_date, end=end_date,freq='M')

for data in datas:
    print(data.strftime('%Y%m'))
    filename = f'focos_mensal_br_{data.strftime('%Y%m')}.csv'

    url = url_base + filename
    output_path = os.path.join(output_dir, filename)

    response = requests.get(url)

    with open(output_path, "wb") as f:
        f.write(response.content)


df = pd.DataFrame({
    'ano_mes': [end_date],
    'data_hora': [pd.Timestamp.now()],
    'status': ['executado']
})

df.to_csv(f'data/control/controle_mensal_queimadas.csv', index=False)