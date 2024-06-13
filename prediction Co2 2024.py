import csv

def data_to_trimestre(value):
    try:
        return float(value) * 4 if value else ""
    except ValueError:
        return value

cols = ['emission de CO2', 'Bioenergy', 'Clean', 'Coal', 'Fossil', 'Gas', 'Hydro', 'Nuclear', 'Other Fossil', 'Other Renewables', 'Solar', 'Wind', 'Wind and solar']

with open('data/final data T1.csv', mode='r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) 


    indices_to_modify = [header.index(col) for col in cols if col in header]

    new_rows = [header]

    for row in reader:
        if row[0] == '2024':
            new_row = row.copy()
            for idx in indices_to_modify:
                new_row[idx] = data_to_trimestre(new_row[idx])
        else:
            new_row = row
        new_rows.append(new_row)

with open('final data 2024.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new_rows)

