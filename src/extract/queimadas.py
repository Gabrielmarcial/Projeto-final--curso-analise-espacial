import pandas as pd
from sqlalchemy import create_engine 
from dotenv import load_dotenv
import os

load_dotenv()

URL_DB = os.getenv('URL_DB') 
engine = create_engine(URL_DB)

def extrac_load_queimadas():

    url_inpe = "https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/mensal/Brasil/"

    df_control = pd.read_csv("data/control/control.csv")

    star_date = df_control['ano_mes'].to_list()[0]
    end_date = pd.Timestamp.today().strftime("%Y-%m")
    datas = pd.date_range(start=star_date, end=end_date,freq='M')


    for data in datas:
        print(data)
        arquivo = f"focos_mensal_br_{data.strftime("%Y%m")}.csv"  
        
        df = pd.read_csv(url_inpe + arquivo)    

        df.to_sql(name='queimadas', con=engine,schema='raw', if_exists='append',index=False)


    df_control = pd.DataFrame({
        "ano_mes": [end_date],
        "data_hora":[pd.Timestamp.now()],
        'status':['Executado']
    })

    df_control.to_csv("data/control/control.csv")