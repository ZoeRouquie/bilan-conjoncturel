import pandas as pd
from decimal import Decimal
from datetime import datetime

data = pd.read_csv("../Downloads/Prix pétrole.csv")
pd.set_option('display.max_rows', None)  


for idx, d in enumerate(data['Month']):
    if not d.startswith("nov.") and not d.startswith("oct."):
        data.at[idx, 'Month'] = datetime.strptime(d, "%b %Y")
        
        
for i in data['Europe Brent Spot Price FOB Dollars per Barrel']:
    i = "{:.2f}".format(i)

print(data)
data.to_csv('Prix pétrole2.csv',  index=False)

print('test')