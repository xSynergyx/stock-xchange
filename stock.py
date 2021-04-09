import requests
from random import randint
import pandas as pd #Add to requirements
import time


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
        print(mega_stock)
        return home_lst
    
test = Stock()
print(test.default())