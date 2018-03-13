import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


stockTicker = 'AAPL'

file = 'data/' + stockTicker + 'compact.json'

data = pd.read_json(file)

print(data)