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


allCoinDict = {}
#calculate(bitcoinList)

bitcoinList= []
# read dataset

path = os.getcwd()
filenames = glob.glob(os.path.join(path, "coinmarketcap*.csv"))
#print(filenames)


for file in filenames:
    df = pd.read_csv(file)
    allCoinDict[df['Pull Time'][0]] = float(df['Price'][0][1:].replace(',',''))
    
bitcoinsPrices = sorted(allCoinDict.items())


for k,v in bitcoinsPrices:
    bitcoinList.append(v)

#print(bitcoinList)

def calculate(stock):
    
    maximum = max(stock)
    profit = 0
    buyIndex = -1
    sellIndex = -1

    for i in range(len(stock)):
        maximum = max(stock[i:])
        buyprice = stock[i]

        if profit < maximum-buyprice:
            buyIndex = i
            profit = maximum - buyprice
            sellIndex = stock.index(maximum)
    print('The time you should buy is '+ bitcoinsPrices[buyIndex][0] )
    print('the price to buy is ' + str(bitcoinsPrices[buyIndex][1]))
    print('The time you should sell is ' + bitcoinsPrices[sellIndex][0] )
    print('the price to sell is ' + str(bitcoinsPrices[sellIndex][1]))
    print('the profit is: ')
    print(profit)


def get_coin_data(coin):

    try:
        conn = sqlite3.connect('crypto.db')  # You can create a new database by changing the name within the quotes
        c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
        c.execute("SELECT PULLTIME, PRICE FROM MARKETDATA WHERE Name = '{}'".format(coin))
        row = c.fetchall()
        print()
        conn.close()
        return row
    except Error as e:
        print(e)
    

def calculate_price(coin):
    stock = [] 
    for i in coin:
        stock.append(float(i[1][1:].replace(',','')))
    print(stock)
    maximum = max(stock)
    profit = 0
    buyIndex = -1
    sellIndex = -1

    for i in range(len(stock)):
        maximum = max(stock[i:])
        buyprice = stock[i]

        if profit < maximum-buyprice:
            buyIndex = i
            profit = maximum - buyprice
            sellIndex = stock.index(maximum)

    print('buy time is')
    print(coin_tuple[buyIndex][0])
    print('buy price is')
    print(coin_tuple[buyIndex][1])
    print('sell time is')
    print(coin_tuple[sellIndex][0])
    print('sell price is')
    print(coin_tuple[sellIndex][1])
    print('the profit is')
    print('$'+str(profit))  


coin='Bitcoin'
coin_tuple = get_coin_data(coin)
calculate_price(coin_tuple)