import requests
import sqlite3
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from decouple import config
import csv
import sqlite3
from sqlite3 import Error
from datetime import datetime
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import selenium as se
from lxml import html
import xlwt 
from xlwt import Workbook 
import csv
import warnings
import lxml
from lxml import html
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from lxml import etree
import time
import pandas as pd
import glob
import os

# read dataset
path = os.getcwd()
filenames = glob.glob(os.path.join(path, "coinmarketcap*.csv"))
print(filenames)

allBitcoinDict = {}
for file in filenames:
    df = pd.read_csv(file)
    print(file)
    print(df)
    #allBitcoinPrice.append(df['Price'][0])
    allBitcoinDict[df['Price'][0]] = df['Percent Change 7 days'][0]
    
#print(allBitcoinDict)
bitcointPrices = []
print({k: v for k, v in sorted(allBitcoinDict.items(), key=lambda item: item[1])})
{bitcointPrices.append(k): v for k, v in sorted(allBitcoinDict.items(), key=lambda item: item[1])}
print(bitcointPrices)

for i in range(bitcointPrices):
    print(i)