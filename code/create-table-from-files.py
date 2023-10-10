import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv(r'C:\Users\Rafi Muhammad\Documents\Bootcamp_DataEngineer\Project3\source\users_w_postal_code.csv', sep = ',')
engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')

df.to_sql("from_file_table", engine)

df_read = pd.read_sql("SELECT * FROM from_file_table", engine)