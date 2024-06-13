import pandas as pd
import matplotlib.pyplot as plt

import csv

def multiplier_par_4(row):
    return [float(x) * 4 if x else "" for x in row]


with open('data/final data.csv', mode='r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) 


    new_rows = [header]


    for row in reader:
        if row[0] == '2024':
            new_row = [row[0]] + multiplier_par_4(row[1:])
        else:
            new_row = row
        new_rows.append(new_row)


with open('final data x4.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new_rows)


# colors = [
#     "#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f",
#     "#bcbd22","#17becf","#1e90ff","#ff1493","#32cd32","#ff4500","#9932cc","#ffd700"
# ]

# for index, c in enumerate(data.drop(columns='Year').columns):
#     plt.figure()  # Crée un nouveau graphique
#     plt.plot(data['Year'], data[c], marker='o', label=c, color=colors[index])
#     plt.title(c)  # Définit le titre du graphique comme le nom de la variable
#     plt.xlabel('Année')
#     plt.ylabel('Valeur')
#     plt.legend()
#     plt.show()

