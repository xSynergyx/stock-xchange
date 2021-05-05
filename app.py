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
USER_LIST = []  #{socket_id: id, name: name}
#{"socket_id": "abc123", "name":"user1"}, {"socket_id": "def123", "name":"user2"}

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
    """ Checks if user connected and sends socket_id """
    print("User connected! " + request.sid)


@SOCKET_IO.on('disconnect')
def on_disconnect():
    """Checks if user is disconnected and removes them from user list"""
    global USER_LIST
    for user in USER_LIST:
        if user['socket_id'] == request.sid:
            USER_LIST.remove(user)
    print('User disconnected!')

    display_list = [user['name'] for user in USER_LIST]
    SOCKET_IO.emit('disconnect',
                   display_list,
                   broadcast=True,
                   include_self=True)


@SOCKET_IO.on('login')
def on_login(data):  #{socket_id: socket_id, username: email}
    """ Sends updated list of active users to client """
    global USER_LIST
    try:  #Checks if socket is in list
        if not any(d['socket_id'] == data['socket_id'] for d in USER_LIST):
            user = {'socket_id': data['socket_id'], 'name': data['username']}
            USER_LIST.append(user)
    except KeyError:
        print("Key Error!")

    display_list = []
    for user in USER_LIST:
        if user['name'] not in display_list:
            display_list.append(user['name'])

    print("list " + str(display_list))
    SOCKET_IO.emit('login', display_list, broadcast=True, include_self=True)


# @SOCKET_IO.on('logout')
# def on_logout(data):
#     """ Removes user from list after logging out"""
#     global USER_LIST
#     for user in USER_LIST:
#         if user['socket_id'] == request.sid:
#             USER_LIST.remove(user)
#     print('User disconnected!')
#     display_list = [user['name'] for user in USER_LIST]
#     SOCKET_IO.emit('disconnect', display_list, broadcast=True, include_self=True)

# @SOCKET_IO.on('like')
# def on_like(data): #{symbol: symbol, like : bool}
#     """Takes stock info with new like number, changes it in the db, and emits to others"""
#     symbol = data['symbol']
#     stock = models.Stocks.query.filter_by(symbols=symbol).first()
#     stock = DB.session.query(models.Stocks).filter(models.Stocks.symbols == symbol).first()
#     if data['like'] is True:
#         stock.likes += 1
#     else:
#         stock.likes -= 1
#     DB.session.commit()
#     #Dont know exactly how what I want to emit: The whole list of stocks from the
#     #home page or just the one stock
#     #SOCKET_IO.emit('like', )


@APP.route('/stocks', methods=['GET'])
def stocks():
    """ Home screen stock lists that shows new stock info every 15 minutes"""
    global USER_LIST
    # With the actual data, we would query an SQLAlchemy model
    # for all records and convert the result to JSON. Haven't looked much
    # into converting SQLAlchemy query results to JSON, but it should be
    # straight forward
    stock = Stock()
    weekdays = [0, 1, 2, 3, 4]
    curr_day = datetime.today().weekday()
    now = datetime.now()
    curr_date = curr_date = now.strftime("%Y-%m-%d")
    open_time = datetime.strptime('{} 9:30AM'.format(curr_date),
                                  '%Y-%m-%d %I:%M%p')
    close_time = datetime.strptime('{} 4:00PM'.format(curr_date),
                                   '%Y-%m-%d %I:%M%p')

    if (curr_day in weekdays and open_time <= now <= close_time):
        # Get the last updated time for the server
        global LAST_UPDATED_TIME

        if (LAST_UPDATED_TIME is None
                or now > LAST_UPDATED_TIME + timedelta(minutes=15)):
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

    display_list = []
    for user in USER_LIST:
        if user['name'] not in display_list:
            display_list.append(user['name'])
    return {"stocks_data": stocks_data, "display_list": display_list}


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
    comment_data = []
    stock_id = None
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

        stock_id = stock_record.id
        # Get the stock info from the DB
        stock_data = {}
        stock_data.update({
            'Symbol': stock_record.symbols,
            'Company': stock_record.stocks_name,
            'High': stock_record.high_stocks,
            'Low': stock_record.low_stocks,
            'Price': stock_record.current_price,
            'Category': stock_record.category
        })

        try:
            news_data = stock_obj.news(stock_data['Company'])
        except KeyError:
            news_data.append({'Error': 'Couldn\'t Retrieve News Data'})

    if stock_id is not None:
        comments = models.Comments.query.filter_by(stocks_column=stock_id).all()
        for comment in comments:
            comment_data.append({
                "username": comment.username,
                "message": comment.comment
            })

        #for comment in comments:
            #page_data.append(comment.comment)
        #print(l)
    #print(page_data)
    page_data['comments'] = comment_data
    return {
        'stock_data': stock_data,
        "page_data": page_data,
        "news_data": news_data
    }


def add_stocks_db(data):
    ''' Insert stock data into the DB '''
    all_stocks = data['allStocks']

    with APP.app_context():
        for i in all_stocks:
            if len(i) == 3:
                symbol = i['Symbol']
                current = i['Price']
                categories = i['Category']

                crypto_record = models.Crypto.query.filter_by(
                    symbols=symbol).first()
                if crypto_record is not None:
                    crypto_record.current_price = current
                else:
                    new_crypto = models.Crypto(symbols=symbol,
                                               current_price=current,
                                               likes=0,
                                               category=categories)
                    DB.session.add(new_crypto)
                DB.session.commit()
            else:
                stockname = i['Company']
                symbol = i['Symbol']
                high = i['High']
                low = i['Low']
                current = i['Price']
                categories = i['Category']
                # Check if the stock record already exists
                stock_record = models.Stocks.query.filter_by(
                    symbols=symbol).first()
                if stock_record is not None:
                    # Update the stock's pricing info in the DB
                    stock_record.high_stocks = high
                    stock_record.low_stocks = low
                    stock_record.current_price = current
                else:
                    # Add the new stock record to the DB
                    new_stock = models.Stocks(stocks_name=stockname,
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
        category_stocks = models.Stocks.query.filter_by(
            category=category).all()
        random_stocks = random.sample(category_stocks,
                                      len(category_stocks))[:4]
        for stock in random_stocks:
            stocks_data['allStocks'].append({
                'Symbol': stock.symbols,
                'Company': stock.stocks_name,
                'High': stock.high_stocks,
                'Low': stock.low_stocks,
                'Price': stock.current_price,
                'Category': stock.category
            })

    #For crypto
    crypto_cat = 'Cryptocurrency'
    category_crypto = models.Crypto.query.filter_by(category=crypto_cat).all()
    random_crypto = random.sample(category_crypto, len(category_crypto))[:4]

    for crypto in random_crypto:
        stocks_data['allStocks'].append({
            'Symbol': crypto.symbols,
            'Price': crypto.current_price,
            'Category': crypto.category
        })
    return stocks_data


@APP.route('/like_stock', methods=['POST'])
def like_stock():
    ''' Insert or delete a record from a user's liked stocks '''
    content = request.get_json(force=True)
    user_symbol = content.get('stock_symbol').upper()
    email = content.get('email')

    print('Email ' + email + ' clicked stock: ' + user_symbol)
    ### Proposed DB Logic ####
    # if a record in the Likes table with matching email & symbol exists:
    #       it's a dislike click so remove that record from the table
    # else:
    #       create a record with client's email / stock symbol in the table
    #check if the like tables has matching email& SYMBOL EXIST
    stock_list = []
    stock_record = models.Person.query.filter_by(username=email).first()
    for i in stock_record.all_stocks:
        s_p = i.stocks
        stock_list.append(s_p)
    if user_symbol not in stock_list:
        with APP.app_context():
            check_symbol = models.Stocks.query.filter_by(
                symbols=user_symbol).first()
            if check_symbol is None:
                increment_like = models.Crypto.query.filter_by(
                    symbols=user_symbol).first()
                increment_like.likes = increment_like.likes + 1
            else:
                increment_like = models.Stocks.query.filter_by(
                    symbols=user_symbol).first()
                increment_like.likes = increment_like.likes + 1
                # Add the symbol to the Like table
            new_user = models.Liketable(person=stock_record.id,
                                        stocks=user_symbol)
            DB.session.add(new_user)
            DB.session.commit()

    else:
        # Delete the User symbol from the database
        with APP.app_context():
            check_symbol = models.Stocks.query.filter_by(
                symbols=user_symbol).first()
            if check_symbol is None:
                decrement_like = models.Crypto.query.filter_by(
                    symbols=user_symbol).first()
                decrement_like.likes = decrement_like.likes - 1
            else:
                decrement_like = models.Stocks.query.filter_by(
                    symbols=user_symbol).first()
                decrement_like.likes = decrement_like.likes - 1
            # Deleting the record from DB
            ndel = models.Liketable.query.filter_by(stocks=user_symbol).first()
            DB.session.delete(ndel)
            DB.session.commit()

    return {}


@APP.route('/login', methods=['POST'])
def login():
    ''' Insert a user record into DB if needed '''
    content = request.get_json(force=True)
    email = content.get('email')
    print('User with email ' + email + ' logged in')

    stock_record = models.Person.query.filter_by(username=email).first()
    with APP.app_context():
        if stock_record is None:
            new_user = models.Person(username=email, bio='')
            DB.session.add(new_user)
            DB.session.commit()
    return {}


@APP.route('/get_liked_stocks', methods=['POST'])
def get_liked_stocks():
    ''' Get a user's liked stocks '''
    content = request.get_json(force=True)
    email = content.get('email')
    print('Get liked stocks for ' + email)
    ### Proposed DB Logic ####
    # Get all records from Likes table matching email
    #       Return records in JSON format like in
    #       test_stock_data.json
    # else:
    #       Return {'myLikedStocks': []}
    test_data = {'myLikedStocks': []}
    stock_record = models.Person.query.filter_by(username=email).first()
    if stock_record is not None:
        for i in stock_record.all_stocks:
            s_p = i.stocks
            search_stocks = models.Stocks.query.filter_by(symbols=s_p).first()
            crypto_search = models.Crypto.query.filter_by(symbols=s_p).first()
            if search_stocks is None:

                if s_p in crypto_search.symbols is not None:
                    test_data['myLikedStocks'].append({
                        'Symbol':
                        crypto_search.symbols,
                        'Price':
                        crypto_search.current_price,
                        'Category':
                        crypto_search.category
                    })
            else:
                if s_p in search_stocks.symbols is not None:

                    test_data['myLikedStocks'].append({
                        'Symbol':
                        search_stocks.symbols,
                        'Company':
                        search_stocks.stocks_name,
                        'High':
                        search_stocks.high_stocks,
                        'Low':
                        search_stocks.low_stocks,
                        'Price':
                        search_stocks.current_price,
                        'Category':
                        search_stocks.category
                    })

    liked_stocks = {}
    # Open a file to write the like stocks
    with open('test_liked_stocks.json', 'w') as json_file:
        json.dump(test_data, json_file, indent=4)
    # Read the file from the JSON file
    with open('test_liked_stocks.json', 'r') as json_file:
        liked_stocks = json.loads(json_file.read())

    return liked_stocks


@APP.route('/submit_comment', methods=['POST'])
def submit_comment():
    ''' Insert a user's comment into the DB '''
    content = request.get_json(force=True)
    email = content.get('email')
    stock_symbol = content.get('stock_symbol')
    comment = content.get('comment')

    print('Email ' + email + ' commented on stock ' + stock_symbol +
          '\nmessage: ' + comment)
    stock = models.Stocks.query.filter_by(symbols=stock_symbol).first()
    #print(stock.stocks_name)
    print(stock.id)
    stock_id = stock.id
    with APP.app_context():
        new_comment = models.Comments(username=email,
                                      comment=comment,
                                      owner=stock.id)

        DB.session.add(new_comment)
        DB.session.commit()
        #DB.session.close()

    comment_data = []
    if stock_id is not None:

        comments = models.Comments.query.filter_by(stocks_column=stock_id).all()
        for comment in comments:
            comment_data.append({
                "username": comment.username,
                "message": comment.comment
            })
        #print(comment_data)
    comment_data = {'message': comment, 'username': email}
    #page_data = {'comment' : comment_data}
    SOCKET_IO.emit('new_comment', comment_data, broadcast=True, include_self=True)

    return {}


@APP.route('/delete_comment', methods=['POST'])
def delete_comment():
    ''' Delete a comment from database'''
    content = request.get_json(force=True)
    email = content.get('email')
    stock_symbol = content.get('stock_symbol')
    comment = content.get('comment')

    stock = models.Stocks.query.filter_by(symbols=stock_symbol).first()
    user_comments = models.Comments.query.filter_by(
        comment=comment, username=email, stocks_column=stock.id).first()
    DB.session.delete(user_comments)
    DB.session.commit()
    

@APP.route('/get_user_profile', methods=['POST'])
def get_user_profile():
    content = request.get_json(force=True)
    email = content.get('email')
    print('Get user profile for ' + email)
    
    myProfile = {'Bio': 'Bio not set'}
    
    profileQuery = models.Person.query.filter_by(username=email).first()
    myProfile['Bio'] = profileQuery.bio
    
    return myProfile
    
@APP.route('/update_bio', methods=['POST'])
def update_bio():
    content = request.get_json(force=True)
    email = content.get('email')
    newBio = content.get('newBio')
    
    print("Bout to update " + email + " bio to " + newBio)
    
    user = models.Person.query.filter_by(username=email).first()
    user.bio = newBio
    DB.session.commit()
    
    return {}


if __name__ == "__main__":
    # Note that we don't call APP.run anymore. We call SOCKET_IO.run with APP arg
    # stocks()
    with APP.app_context():
        DB.create_all()
    SOCKET_IO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
