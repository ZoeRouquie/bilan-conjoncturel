import matplotlib.pyplot as plt
import pandas as pd


data =  pd.read_csv('data/production electricite.csv')
colors = [
    "#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f",
    "#bcbd22","#17becf","#1e90ff","#ff1493","#32cd32","#ff4500","#9932cc","#ffd700"
]

plt.figure(figsize=(10, 6))

# Tracer chaque colonne sur le même graphique
for index, c in enumerate(data.drop(columns=['Total']).columns):
    plt.plot(data['date'], data[c], marker='o', label=c, color=colors[index % len(colors)])

# Ajouter des titres et des légendes
plt.title('Évolution des différentes sources d\'énergie')
plt.xlabel('Mois')
plt.ylabel('Valeur')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Légende à l'extérieur du graphique

# Afficher le graphique
plt.tight_layout()
plt.show()

