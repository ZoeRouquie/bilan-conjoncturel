import pandas as pd
file_path = './data/quotas prix Europe.csv'

data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'], format='%d.%m.%Y')
data['Year'] = data['Date'].dt.year

numeric_columns = ['Domestic Currency (EUR)', 'Exchange Rate (USD)', 'EUR_USD', 'EUR_EUR']

for col in numeric_columns:
    data[col] = data[col].str.replace(',', '.')
    data[col] = data[col].astype(float)
data = data.drop(columns=['Date as Text'])

grouped_data = data.groupby('Year')[numeric_columns].mean().reset_index()


grouped_data.to_csv('prix quota EUrope annuel.csv', index=False)