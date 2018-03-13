import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config/config.ini')

apiKey = config.get('auth', 'apiKey')


stockTicker = 'AAPL'

URL = 'https://www.alphavantage.co/query?' \
      'function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + stockTicker + '&outputsize=full&apikey=' + apiKey

response = requests.get(URL)
print(response)

nFile = open("data/" + stockTicker + "compact.json", "w+")
nFile.write(response.text)
nFile.close()
print("Data saved to: " + str(nFile.name))
