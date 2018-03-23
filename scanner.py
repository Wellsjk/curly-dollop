import pandas as pd
import json
import matplotlib.pyplot as plt
import csv

thresholdPercent = .02
days2check = 5

with open('data/stockList.csv', 'r') as d:
    reader = csv.reader(d)
    stockList = list(reader)
    d.close()

i = 0
p = 0
stockList = stockList[0]


while p < len(stockList):
    stockTicker = stockList[p]
    file = 'data/' + stockTicker + 'compact.csv'
    data = pd.read_csv(file)


    # data.index = data['timestamp']
    stockData = data[['timestamp', 'close']]

    thresholdAmount = stockData['close'][days2check] - (stockData['close'][0]*thresholdPercent)
    print('Threshold amount: ' + str(thresholdAmount) + '  For: ' + stockTicker)
    i = days2check
    while i > 0:
        if stockData['close'][i] < thresholdAmount:
            print('!Dropped more than threshold on: ' + str(stockData['timestamp'][i]) + ' Price: ' + str(stockData['close'][i])+ '!!!!!!')
            i = i - 1
        else:
           # print('did not drop more than threshold, price: ' + str(stockData['close'][i])+ ' Date: ' + str(stockData['timestamp'][i]))
            i = i - 1

    p = p + 1


