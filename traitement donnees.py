import pandas as pd
file_path = 'data\prix petrole.csv'

data = pd.read_csv(file_path)

data['Month'] =pd.to_datetime(data['Month'], format='%d/%m/%Y')
data['Year'] = data['Month'].dt.year

grouped_data = data.groupby('Year')['Europe Brent Spot Price FOB Dollars per Barrel'].mean().reset_index()
grouped_data.to_csv('data\prix pétrole.csv', index=False)