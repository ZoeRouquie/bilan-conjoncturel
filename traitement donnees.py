import pandas as pd

file_path = 'data\EU génération éléectricité.csv'

data = pd.read_csv(file_path, sep = ';')


data['Year'] = pd.to_datetime(data['date']).dt.year

# Utiliser pivot_table pour restructurer les données
df_pivot = data.pivot_table(index='Year', columns='variable', values='generation_twh', aggfunc='sum').reset_index()

# Afficher le DataFrame résultant

df_pivot.to_csv(file_path,index= False)
print('done')