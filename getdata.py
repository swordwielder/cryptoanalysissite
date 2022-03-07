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
#print(filenames)

allBitcoinDict = {}
for file in filenames:
    df = pd.read_csv(file)
    #print(file)
    #print(df)
    #allBitcoinPrice.append(df['Price'][0])
    allBitcoinDict[df['Percent Change 7 days'][0]] = float(df['Price'][0][1:].replace(',',''))
    
#print(allBitcoinDict)
bitcoinsPrices = sorted(allBitcoinDict.items())
#print(bitcoinsPrices)


bitcoinList= []
for k,v in bitcoinsPrices:
    bitcoinList.append(v)


def calculate(stock):
    

    maximum = max(stock)
    profit = 0
    buyIndex = -1


    maxBuyProfit = 0
    for i in range(len(stock)):
        maximum = max(stock[i:])
        buyprice = stock[i]

        if profit < maximum-buyprice:
            buyIndex = i
            profit = maximum - buyprice
            sellIndex = stock.index(maximum)
    print('The time you should buy is '+ bitcoinsPrices[buyIndex][0] )
    print('The time you should sell is ' + bitcoinsPrices[sellIndex][0] )
    print('the profit is: ')
    print(profit)




calculate(bitcoinList)

