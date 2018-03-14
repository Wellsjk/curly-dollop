import pandas as pd
import json
import matplotlib.pyplot as plt


stockTicker = 'AAPL'
file = 'data/' + stockTicker + 'compact.csv'
data = pd.read_csv(file)

# data.index = data['timestamp']
print(data[['timestamp', 'close']])

