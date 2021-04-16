'''
    app.py
    Server file.
'''

import os
import json
from datetime import datetime, timedelta
from flask import Flask, send_from_directory, request, session
from stock import Stock
from flask_socketio import SocketIO
from stock_utils import parse_api_data
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv,find_dotenv


APP = Flask(__name__, static_folder='./build/static')
SOCKET_IO = SocketIO()
load_dotenv(find_dotenv())
APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)
import models
# DB.create_all()
# Datetime object to store the last time the database was updated
# Server-wide variable compared to each incoming client-side request
LAST_UPDATED_TIME = None
stocks_List={'stocks_name':[] , 'symbols': [], 'high_stocks':[], 'lows_stocks':[], 'like':[], 'comments':[]
    }

COR_S = CORS(APP, resources={r"/*": {"origins": "*"}})
SOCKET_IO = SocketIO(APP,
                     cors_allowed_origins="*",
                     json=json,
                     manage_session=False)
    
@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    """ index """
    return send_from_directory('./build', filename)

# When a client connects from this Socket connection, this function is run
@SOCKET_IO.on('connect')
def on_connect():
    """ checks if user connected and dsiplay the leaderboard """
    print('User connected!')

# When a client disconnects from this Socket connection, this function is run
@SOCKET_IO.on('disconnect')
def on_disconnect():
    """CHecks if user is disconnected """
    print('User disconnected!')


@APP.route('/stocks', methods=['GET'])
def stocks():
    """ Home screen stock lists that shows new stock info every 15 minutes"""
    # With the actual data, we would query an SQLAlchemy model
    # for all records and convert the result to JSON. Haven't looked much
    # into converting SQLAlchemy query results to JSON, but it should be
    # straight forward
    stock = Stock()
    weekdays = [0, 1, 2, 3, 4]
    curr_day = datetime.today().weekday()
    now = datetime.now()
    curr_date = curr_date = now.strftime("%Y-%m-%d")
    open_time = datetime.strptime('{} 9:30AM EST'.format(curr_date), '%Y-%m-%d %I:%M%p %Z')
    close_time = datetime.strptime('{} 4:00PM EST'.format(curr_date), '%Y-%m-%d %I:%M%p %Z')

    if (
            curr_day in weekdays
            and open_time <= now <= close_time
    ):
        global LAST_UPDATED_TIME

        if (
                LAST_UPDATED_TIME is None
                or now > LAST_UPDATED_TIME + timedelta(minutes=15)
        ):
            # Call the API to update records in the database
            api_data = stock.default()
            LAST_UPDATED_TIME = now
            #Add data into db and commit data
            stocks_data = parse_api_data(api_data)
            with open('test_stock_data3.json', 'w') as json_file:
                json.dump(stocks_data, json_file)
        else:
            # 15 hasn't passed since last database update
            # Read from database only
            # Gather 4 random stocks from each category
            with open('test_stock_data3.json', 'r') as json_file:
                stocks_data = json.loads(json_file.read())
    else:
        print("After hour stock data")
        # Gather random 4 stocks from db
        # For Testing
        with open('test_stock_data3.json', 'r') as json_file:
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
    #     if curr_day in weekdays:

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
    with open('test_stock_data3.json', 'r') as json_file:
        stocks_data = json.loads(json_file.read())
        for stock in stocks_data['allStocks']:
            if stock['Symbol'] == user_symbol:
                stock_data = stock
                print(stock_data)

    stock_obj = Stock()
    news = stock_obj.news(stock_data['Company'])
    return {"stock_data": stock_data, "page_data": page_data, "news_data": news}


@APP.route('/search', methods=['POST'])
def search():
    ''' Processes user's request and returns the stock information '''
    return None
    ###### Proposed Logic Below #######
    # if Stock_Symbol is in database:
    #  if today is a weekday and during market hours:
    #       if it's been 15 minutes since the DB was updated:
    #           call API, update DB, return stock info in JSON format
    #       else:
    #           return Stock Info already in DB in JSON format
    #   else not a weekday:
    #       return Stock info already in DB in JSON format
    # else Stock_Symbol isn't in DB:
    #   if it's a weekday and during market hours:
    #       call API with user's request, add new Stock record to DB,
    #       return data to client in JSON format
    #   else:
    #       return stock info not available message


stock = Stock()
api_data = stock.default()
# print(api_data)
stocks_data = parse_api_data(api_data)
# print(json.dumps(stocks_data, indent=4))

# # def add_stocks_db(data):
# x=stocks_data['allStocks']
# for i in x:
#     stockname=i['Company']
#     symbol=i['Symbol']
#     high=i['High']
#     low=i['Low']
#     categories=i['Category']
       
       
#         #Add to db
#     stocks_db= models.Stocks.query.all()
#     new_Stock=models.Stocks(stock_name=stockname, symbols=symbol , high_stocks=high, low_stocks=low, likes=100 , category=categories)
#     DB.session.add(new_Stock)
#     DB.session.commit()
        
        
# # add_stocks_db(stocks_data)


if __name__ == "__main__":
    DB.create_all()
    # Note that we don't call APP.run anymore. We call SOCKET_IO.run with APP arg
    SOCKET_IO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
