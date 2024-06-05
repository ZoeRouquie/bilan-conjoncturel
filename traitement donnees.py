import pandas as pd
file_path = 'data\prix quota Europe annuel.csv'

data = pd.read_csv(file_path)

data = data.drop('Exchange Rate (USD)')

data = data.drop('EUR_USD')

data = data.drop('EUR_EUR')

data.to_csv(file_path)