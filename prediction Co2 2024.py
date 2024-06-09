import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  
df = pd.read_csv('data/bilan conjoncturel EU ETS datas - data.csv')

data = df.dropna()
X = data.drop(columns=['Year', 'emission de CO2'])
y = data['emission de CO2']

# Créer et ajuster le modèle de régression linéaire multiple
model = LinearRegression()
model.fit(X, y)

# Préparer les données pour l'année 2024
X_2024 = df.tail(1)
X_2024 = X_2024.drop(columns = ['Year','emission de CO2'])


prediction_2024 = model.predict(X_2024)
print(prediction_2024)

df.loc[df['Year'] == 2024, 'emission de CO2'] = prediction_2024[0]

# Afficher la courbe d'émission de CO2
plt.plot(df['Year'], df['emission de CO2'], marker='o')
plt.xlabel('Year')
plt.ylabel('emission de CO2')
plt.title('Prediction of CO2 Emissions for 2024')
plt.grid(True)
plt.show()