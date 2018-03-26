from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

tickers = 'AAPL'

data_source = 'google'

startDate = '2004-01-01'
endDate = '2018-01-01'

stockDate = data.DataReader(tickers, data_source,startDate,endDate)

