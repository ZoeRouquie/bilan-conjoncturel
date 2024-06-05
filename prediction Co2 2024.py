import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('data\data final.csv')


features = ['Europe Brent Spot Price FOB Dollars per Barrel', 'prix quotas', 'prix electricité par kwt', 'production energie']
target = 'emission de CO2'
data = data.dropna(inplace=True)

print(data)
"""X = data[features]
y = data[target]

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle de régression linéaire multivariée
model = LinearRegression()
model.fit(X_train, y_train)

# Évaluer le modèle
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Prédire les émissions de CO2 pour l'année 2024
# Créez un DataFrame avec les caractéristiques pour 2024
X_2024 = pd.DataFrame({'Europe Brent Spot Price FOB Dollars per Barrel': [None],
                       'prix quotas': [None],
                       'prix electricité par kwt': [None],
                       'Year': [2024]})

# Faites une prédiction
prediction_2024 = model.predict(X_2024)
print('Prédiction pour 2024:', prediction_2024)





"""