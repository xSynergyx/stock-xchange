'''
    app.py

    Server file.
'''

import os
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

SOCKET_IO = SocketIO()

APP = Flask(__name__, static_folder='./build/static')
APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)
import stock_databse


# Displaying on UI
def display_on_ui(stocks_name, symbols, high_stocks, lows_stocks,comments):
    all_stocks=stock_databse.Stocks.query.all()
    stocks_name=[]
    symbols=[]
    high_stocks=[]
    low_stocks=[]
    comments=[]
    for data in all_stocks:
        stocks_name.append(data.stocks_name)
        symbols.append(data.symbols)
        high_stocks.append(data.high_stocks)
        low_stocks.append(data.low_stocks)
        comments.append(data.comments)
    return stocks_name,symbols,high_stocks,low_stocks,comments
    
    
@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    """ index """
    return send_from_directory('./build', filename)


APP.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)

if __name__ == "__main__":
    DB.create_all()
    # Note that we don't call APP.run anymore. We call SOCKET_IO.run with APP arg
    SOCKET_IO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
