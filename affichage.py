import matplotlib.pyplot as plt
import pandas as pd


data =  pd.read_csv('data/final data T1.csv')
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

