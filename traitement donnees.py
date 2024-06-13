import pandas as pd

file_path = 'data\production elec mensuelle.csv'

data = pd.read_csv(file_path, sep = ';')


df_pivot = data.pivot_table(index='date', columns='variable', values='generation_twh', aggfunc='sum').reset_index()

df_pivot.to_csv('data\production electricite.csv',index= False)
print('done')

