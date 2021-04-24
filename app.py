'''
    app.py
    Server file.
'''

import os
import json
import random
from datetime import datetime, timedelta
from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from stock import Stock
from database import DB
from stock_utils import parse_api_data

APP = Flask(__name__, static_folder='./build/static')
load_dotenv(find_dotenv())
APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB.init_app(APP)
import models

# Datetime object to store the last time the database was updated
# Server-wide variable compared to each incoming client-side request
LAST_UPDATED_TIME = None
USER_LIST = [] #{socket_id: id, player_name: name}

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
    """ checks if user connected"""
    print('User connected!')
    
    
# When a client disconnects from this Socket connection, this function is run
@SOCKET_IO.on('disconnect')
def on_disconnect():
    """CHecks if user is disconnected """
    print('User disconnected!')
    

@SOCKET_IO.on('login')
def on_login(data):
    global USER_LIST
    socket_id = request.sid
    if not any(d['socket_id'] == data['socket_id'] for d in USER_LIST): #Checks if socket is in list
        user = {'socket_id': data['socket_id'] , 'name' : data['name']}
        USER_LIST.append(user)
    sid = {'socket_id': socket_id} #sends id to client
    display_list = [user['name'] for user in USER_LIST]
    SOCKET_IO.emit('login', display_list, broadcast=True, include_self=True)

@SOCKET_IO.on('like')
def on_like(data):
    """Takes stock info with new like number, changes it in the db, and emits to others"""
    new_like = data['likes']
    #SOCKET_IO.emit('like', )

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
    open_time = datetime.strptime('{} 9:30AM'.format(curr_date), '%Y-%m-%d %I:%M%p')
    close_time = datetime.strptime('{} 4:00PM'.format(curr_date), '%Y-%m-%d %I:%M%p')

    if (
            curr_day in weekdays
            and open_time <= now <= close_time
    ):
        # Get the last updated time for the server
        global LAST_UPDATED_TIME

        if (
                LAST_UPDATED_TIME is None
                or now > LAST_UPDATED_TIME + timedelta(minutes=15)
        ):
            # Call the API to update records in the database
            api_data = stock.default()
            LAST_UPDATED_TIME = now
            stocks_data = parse_api_data(api_data)
            # Add data into db and commit data
            add_stocks_db(stocks_data)
        else:
            # 15 hasn't passed since last database update
            # Read from database only
            # Gather 4 random stocks from each category
            stocks_data = get_random_stocks_db()
    else:
        if LAST_UPDATED_TIME is None:
            # Just in case it's not during market hours
            # and the database could be empty
            api_data = stock.default()
            LAST_UPDATED_TIME = now
            stocks_data = parse_api_data(api_data)
            # Add data into db and commit data
            add_stocks_db(stocks_data)
        else:
            print("After hour stock data")
            stocks_data = get_random_stocks_db()

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
    news_data = []
    page_data = {}
    stock_data = {}
    # Get the stock id sent from the client side
    content = request.get_json(force=True)
    user_symbol = content.get('stock_symbol').upper()
    stock_obj = Stock()

    # Check if the request stock exists in the database
    stock_record = models.Stocks.query.filter_by(symbols=user_symbol).first()
    if stock_record is None:
        # Query the API for user requested stock
        api_data = stock_obj.search([user_symbol], None)

        if 'Not Found' in api_data.values():
            stock_data.update({'Error': 'No Results Found'})
        else:
            stock_data = parse_api_data(api_data)
            add_stocks_db(stock_data)

    else:
        # To get page data, we would search the database's Comments table
        # to get all of the comment records matching the stock_symbol passed in via the client side
        # Convert this info. to JSON format and send it back to the client
        with open('test_stock_page.json', 'r') as json_file:
            page_data = json.loads(json_file.read())

        # Get the stock info from the DB
        stock_data = {}
        stock_data.update({
            'Symbol': stock_record.symbols,
            'Company': stock_record.stocks_name,
            'High': stock_record.high_stocks,
            'Low': stock_record.low_stocks,
            'Price': stock_record.current_price,
            'Category': stock_record.category})

        try:
            news_data = stock_obj.news(stock_data['Company'])
        except KeyError:
            news_data.append({'Error': 'Couldn\'t Retrieve News Data'})

    return {'stock_data': stock_data, "page_data": page_data, "news_data": news_data}


def add_stocks_db(data):
    ''' Insert stock data into the DB '''
    all_stocks = data['allStocks']
    for i in all_stocks:
        stockname = i['Company']
        symbol = i['Symbol']
        high = i['High']
        low = i['Low']
        current = i['Price']
        categories = i['Category']

        # Check if the stock record already exists
        stock_record = models.Stocks.query.filter_by(symbols=symbol).first()
        if stock_record is not None:
            # Update the stock's pricing info in the DB
            stock_record.high_stocks = high
            stock_record.low_stocks = low
            stock_record.current_price = current
        else:
            # Add the new stock record to the DB
            new_stock = models.Stocks(
                stocks_name=stockname,
                symbols=symbol,
                high_stocks=high,
                low_stocks=low,
                current_price=current,
                likes=0,
                category=categories)

            DB.session.add(new_stock)
        DB.session.commit()


def get_random_stocks_db():
    ''' Get 4 random stocks from each of the predefined categories '''
    stocks_data = {'allStocks': []}

    for category in ['Mega', 'Finance', 'Energy', 'Utilities', 'Tech']:
        category_stocks = models.Stocks.query.filter_by(category=category).all()
        random_stocks = random.sample(category_stocks, len(category_stocks))[:4]
        for stock in random_stocks:
            stocks_data['allStocks'].append({
                'Symbol': stock.symbols,
                'Company': stock.stocks_name,
                'High': stock.high_stocks,
                'Low': stock.low_stocks,
                'Price': stock.current_price,
                'Category': stock.category
            })

    return stocks_data


if __name__ == "__main__":
    # Note that we don't call APP.run anymore. We call SOCKET_IO.run with APP arg
    SOCKET_IO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
