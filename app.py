'''
    app.py

    Server file.
'''

import os
import json
import time
from datetime import datetime, timedelta
from flask import Flask, send_from_directory, request
from stock import Stock
from stock_utils import *

# Make a global variable called last_updated_time
# If the current time is 15 minutes past this variable
# do the API calls and update database. Else, solely retrieve from db

APP = Flask(__name__, static_folder='./build/static')

# Datetime object to store the last time the database was updated
# Server-wide variable compared to each incoming client-side request
last_updated_time = None

@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    """ index """
    return send_from_directory('./build', filename)

@APP.route('/stocks', methods=['GET'])
def stocks():
    """ Home screen stock lists that shows new stock info every 15 minutes"""
    # With the actual data, we would query an SQLAlchemy model
    # for all records and convert the result to JSON. Haven't looked much
    # into converting SQLAlchemy query results to JSON, but it should be
    # straight forward

    # This method of searching a hardcoded JSON file is just for testing.

    # stocks_data = {}
    # with open('test_stock_data.json', 'r') as json_file:
    #     stocks_data = json.loads(json_file.read())
    stocks_data = {"allStocks": [{"Symbol": "NIO", "Name": "NIO Limited", "Price (Intraday)": "46.95", "Change": "+1.59", "% Change": "+3.50%", "Volume": "271.313M", "Avg Vol (3 month)": "158.175M", "Market Cap": "63.951B", "PE Ratio (TTM)": "N/A", "52 Week Range": "None", "id": 1}]} #Populate dictionary with 4 of each most recent stock in each group
    stock = Stock()
    weekdays = [0, 1, 2, 3, 4]
    curr_day = datetime.today().weekday()
    now = datetime.now()
    curr_date = curr_date = now.strftime("%Y-%m-%d")
    open_time = datetime.strptime('{} 9:30AM EST'.format(curr_date), '%Y-%m-%d %I:%M%p %Z')
    close_time = datetime.strptime('{} 4:00PM EST'.format(curr_date), '%Y-%m-%d %I:%M%p %Z')
    time_lst = []
    time_lst.append(open_time)
    while True:
        open_time += timedelta(minutes=15)
        time_lst.append(open_time)
        if open_time == close_time:
            open_time = datetime.strptime('{} 9:30AM EST'.format(curr_date), '%Y-%m-%d %I:%M%p %Z')
            break
    
    #if (curr_day in weekdays) and (now >= open_time and now <= close_time):

    global last_updated_time
    if (last_updated_time == None) or (now > last_updated_time + timedelta(minutes=15)):
        # Call the API to update records in the database
        api_data = stock.default()
        last_updated_time = now
        #Add data into db and commit data
        #stocks_data = parse_api_data(data)
        stocks_data = parse_api_data(api_data)
        print(parse_api_data(api_data))

    if curr_day in weekdays and open_time <= now <= close_time:
        if now in time_lst: 
            stocks_info = stock.default()
            #Add data into db and commit data
            print(stocks_data)
            stocks_data = {} #Populate dictionary with 4 of each most recent stock in each group
    else:
        print("After hour stock data")
        #Gather random 4 stocks from db

        # For Testing
        with open('test_stock_data2.json', 'r') as json_file:
            stocks_data = json.loads(json_file.read())
    return stocks_data

@APP.route('/stock_page', methods=['POST'])
def stock_page():
    """ Function that sends individual stock info to stock page """

    # We're assuming that the requested stock will exist in the database
    # when the stock page link is accessed. So we simply query the database
    # for the symbol request sent by the client

    # stock = Stock()
    # weekdays = [0,1,2,3,4] 
    # curr_day = datetime.datetime.today().weekday()
    # while True:
    #     if curr_day in weekdays:
    #         page_data = stock.default()
    #         print(page_data)   
    #         #Include line where stock info is stored into db between api call times
            
    # Get the stock id sent from the client side
    user_symbol = request.get_json()['stock_symbol']
    # page_data = {}

    # To get page data, we would search the database's Comments table
    # to get all of the comment records matching the stock_symbol passed in via the client side
    # Convert this info. to JSON format and send it back to the client
    with open('test_stock_page.json', 'r') as json_file:
        page_data = json.loads(json_file.read())

    # To get stock data, we would search the database for stock records matching the stock
    # symbol passed in from the client side

    # If a record exists for that symbol, get the stock info. and convert it to
    #JSON and return to the client

    # If a record matching the symbol doesn't exist, query the API for the requested stock,
    # get info. in JSON, and return to client
    stock_data = {}
    with open('test_stock_data2.json', 'r') as json_file:
        stocks_data = json.loads(json_file.read())
        for category in ['Mega', 'Tech', 'Energy', 'Utilities', 'Finance']:
            for stock in stocks_data[category]:
                if stock['Symbol'] == user_symbol:
                    stock_data = stock
                    print(stock_data)

    return {"stock_data": stock_data, "page_data": page_data}

APP.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)
