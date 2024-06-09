import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  
df = pd.read_csv('data/bilan conjoncturel EU ETS datas - data.csv')

data = df.dropna()
X = data.drop(columns=['Year', 'emission de CO2'])
y = data['emission de CO2']

model1 = LinearRegression()

models = {'Linear Regression': model1}
scores = {}

for model_name, model in models.items():
    cv_scores = cross_val_score(model, X, y, cv=5)  
    scores[model_name] = cv_scores.mean()

best_model_name = max(scores, key=scores.get)
best_model = models[best_model_name]

best_model.fit(X, y)
X_2024 = df.tail(1)
X_2024 = X_2024.drop(columns = ['Year','emission de CO2'])


prediction_2024 = best_model.predict(X_2024)
print(prediction_2024)

df.loc[df['Year'] == 2024, 'emission de CO2'] = prediction_2024[0]

new_row = df.tail(1)
data = data._append(new_row, ignore_index=True)

# Afficher la courbe d'émission de CO2
# plt.plot(data['Year'], data['emission de CO2'], marker='o', label='Emission de CO2', color='blue')


colors = [
    "#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f",
    "#bcbd22","#17becf","#1e90ff","#ff1493","#32cd32","#ff4500","#9932cc","#ffd700"
]

for index, c in enumerate(data.drop(columns='Year').columns):
    plt.figure()  # Crée un nouveau graphique
    plt.plot(data['Year'], data[c], marker='o', label=c, color=colors[index])
    plt.title(c)  # Définit le titre du graphique comme le nom de la variable
    plt.xlabel('Année')
    plt.ylabel('Valeur')
    plt.legend()
    plt.show()