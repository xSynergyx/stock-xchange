"""
    stock.py

    Stock class file.
"""
from random import randint
import requests
import pandas as pd #Add to requirements pandas and numpy
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Stock:
    """Class object gathers stock information and news for selected companies"""
    IEX_SANDBOX_URL = "https://sandbox.iexapis.com/stable/stock/market/batch?"
    NYT_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    
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
        # print('mega: ' + str(mega_stock))
        # print('tech: ' + str(tech_stock))
        # print('energy: ' + str(energy_stock))
        # print('finance: ' + str(finance_stock))
        # print('public utilities: ' + str(utilities_stock))
        home_lst.append({'Mega': self.search(mega_stock)})
        return home_lst

    def search(self, query):
        """Takes list of symbols, and gathers stock information"""
        data = {}
        symbols = None
        if len(query) == 1:
            symbols = query[0]
        else:
            symbols = query[0]
            for i in range(1, len(query)):
                symbols += ',{}'.format(query[i])
        params = {
         'symbols': symbols,
         'types': 'quote',
         'token': os.getenv('IEX_CLOUD_SANDBOX_KEY')
        }
        stocks = [x.upper() for x in query] #capatalize symbols for json file
        response = requests.get(self.IEX_SANDBOX_URL, params=params)
        response_json = response.json()
        print(response_json)
        
    def news(self, query):
        """ Gathers articles related to company after click """
        pass

TEST = Stock()
print(TEST.default())