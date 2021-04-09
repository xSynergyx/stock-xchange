"""
    stock.py

    Stock class file.
"""
import requests
from random import randint
import pandas as pd #Add to requirements pandas and numpy
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Stock:
    BASE_URL = "https://sandbox.iexapis.com/stable/stock/market/batch?"
    
    def symbols(self, csv_file):
        """Gathers symbols into list from csv file"""
        df = pd.read_csv(csv_file)
        symbols = df['Symbol']
        stock_lst = []
        num_list = []
        while len(stock_lst) < 3:
            num = randint(0, len(symbols)-1)
            if num not in num_list:
                stock_lst.append(symbols[num])
                num_list.append(num)
        return stock_lst
   
    def default(self):
        """Default homescreen with stock information"""
        home_lst = []
        mega_stock = self.symbols('mega.csv')
        tech_stock = self.symbols('tech.csv')
        energy_stock = self.symbols('energy.csv')
        finance_stock = self.symbols('finance.csv')
        utilities_stock = self.symbols('pub_utilities.csv')
        print('mega: ' + str(mega_stock))
        print('tech: ' + str(tech_stock))
        print('energy: ' + str(energy_stock))
        print('finance: ' + str(finance_stock))
        print('public utilities: ' + str(utilities_stock))
        return home_lst

    def search(self, query):
        """Takes list of symbols, and gathers stock information"""
        data = {}
        symbols = None
        params = {
         'symbols': symbols,
         'types': 'quote',
         'token': os.getenv('IEX_CLOUD_SANDBOX_KEY')
        }
        pass
   
    def news(self, query):
        """ Gathers articles related to company after click """
        pass

    
test = Stock()
print(test.default())