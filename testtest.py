from databaseIniti import exporter
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:123qweasdzxcSq@localhost/elfateh')
df = pd.read_excel(r'D:\monymovment\Cashflows\Excel_files\SBJRNLITMRPTTAX.xls')
df.to_sql('price', con=engine, if_exists='replace', index=False)
