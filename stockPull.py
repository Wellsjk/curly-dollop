import requests
import csv
import numpy
from configparser import ConfigParser

config = ConfigParser()
config.read('config/config.ini')
apiKey = config.get('auth', 'apiKey')
with open('data/stockList.csv', 'r') as d:
    reader = csv.reader(d)
    stockList = list(reader)
    d.close()

i = 0
stockList = stockList[0]


while i < len(stockList):
    stockTicker = stockList[i]

    URL = 'https://www.alphavantage.co/query?' \
          'function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + stockTicker + '&outputsize=compact&apikey=' + apiKey

    response = requests.get(URL)
    print(response)

    nFile = open("data/" + stockTicker + "compact.json", "w+")
    nFile.write(response.text)
    nFile.close()
    print("Data saved to: " + str(nFile.name))
    i = i + 1

print('\nCompleted Data Collection for ' + str(i+1) + ' stocks.')
