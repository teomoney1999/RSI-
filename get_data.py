import requests
import json
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import datetime as dt 

root_url = 'https://api.binance.com/api/v1/klines'

# Get the bar for a specific symbol and timeframe
symbol = 'STEEMETH'

interval = '1h'

url = root_url + '?symbol=' + symbol +'&inverval=' + interval
print(url)

data = json.load(requests.get(url).text)