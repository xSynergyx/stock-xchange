"""
    stock.py

    Stock class file.
"""
from random import randint
import os
from dotenv import load_dotenv, find_dotenv
#import time
import requests
import pandas as pd #Add to requirements pandas and numpy

load_dotenv(find_dotenv())

def symbols(csv_file):
    """Gathers symbols into list from csv file"""
    file = pd.read_csv(csv_file)
    symbol = file['Symbol']
    stock_lst = []
    num_list = []
    while len(stock_lst) < 4:
        num = randint(0, len(symbol)-1)
        if num not in num_list:
            stock_lst.append(symbol[num])
            num_list.append(num)
    return stock_lst

class Stock:
    """Class object gathers stock information and news for selected companies"""
    IEX_SANDBOX_URL = "https://sandbox.iexapis.com/stable/stock/market/batch?"
    IEX_SANDBOX_NEWS_URL = "https://sandbox.iexapis.com/stable/stock/market/batch?"
    NYT_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

    def default(self):
        """Default homescreen with stock information"""
        home_lst = []
        mega_stock = symbols('stock_categories/mega.csv')
        tech_stock = symbols('stock_categories/tech.csv')
        energy_stock = symbols('stock_categories/energy.csv')
        finance_stock = symbols('stock_categories/finance.csv')
        utilities_stock = symbols('stock_categories/pub_utilities.csv')
        home_lst.append({'Mega': self.search(mega_stock)})
        home_lst.append({'Tech': self.search(tech_stock)})
        home_lst.append({'Energy': self.search(energy_stock)})
        home_lst.append({'Utilities': self.search(utilities_stock)})
        home_lst.append({'Finance': self.search(finance_stock)})
        return home_lst

    def search(self, query):
        """Takes list of symbols, and gathers stock information"""
        data = {}
        stock_symbols = None
        if len(query) == 1:
            stock_symbols = query[0]
        else:
            stock_symbols = query[0]
            for i in range(1, len(query)):
                stock_symbols += ',{}'.format(query[i])
        params = {
            'symbols': stock_symbols,
            'types': 'quote',
            'token': os.getenv('IEX_CLOUD_SANDBOX_KEY')
        }
        stocks = [x.upper() for x in query] #capatalize symbols for json file
        response = requests.get(self.IEX_SANDBOX_URL, params=params)

        if response.status_code == 404: #Resource not found
            data[query[0]] = 'Not Found'
            return data
        response_json = response.json()
        if response_json[query[0]]['quote'] is None: #200 status but still not valid stock symbol
            data[query[0]] = 'Not Found'
            return data
        #print(response_json)
        for stock in stocks:
            stock_dict = {}
            stock_quote = response_json[stock]['quote']
            stock_dict['Symbol'] = stock
            stock_dict['Company'] = stock_quote['companyName']
            stock_dict['High'] = stock_quote['high']
            stock_dict['Low'] = stock_quote['low']
            stock_dict['Price'] = stock_quote['latestPrice']
            data[stock] = stock_dict
        return data

    def news(self, stock):
        """ Gathers five articles related to company after click with NYT API
            Use IEX API in case of KeyError from NYT reaching minute request limit.
        """
        news = []
        try:
            params = {
                'q' : stock + ' ',
                'news_desk' : 'Business',
                'api-key': os.getenv('NYT_KEY')
            }
            response = requests.get(self.NYT_URL, params=params)
            print(response)
            if response.status_code == 429: #Too many requests
                raise KeyError("Response 429")
            data = response.json()
            for i in range(5):
                #print(data['response']['docs'][i]['headline']['main'])
                news.append(data['response']['docs'][i]['headline']['main'])
            #print(data)
        except KeyError:
            params = {
                'symbols': stock,
                'token': os.getenv('IEX_CLOUD_SANDBOX_KEY'),
                'types': 'news',
                'last': 5
            }
            response = requests.get(self.IEX_SANDBOX_NEWS_URL, params=params)
            print(response)
            data = response.json()
            #print(data[stock])
            stock_news = data[stock]['news']
            for headline in stock_news:
                #print(str(headline['headline']))
                news.append(headline['headline'])
        except ValueError: #simplejson.errors.JSONDecodeError
            print("Decode JSON failed")
            news = ["Refresh page"]
        print(news)
        return news

# TEST = Stock()
# for count in range(20):
#     TEST.news('AAPL')
# #print(TEST.default())
