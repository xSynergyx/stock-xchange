'''
    app.py

    Server file.
'''

import os
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv,find_dotenv

SOCKET_IO = SocketIO()

APP = Flask(__name__, static_folder='./build/static')
APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)
import models

stocks_List={'stocks_name':[] , 'symbols': [], 'high_stocks':[], 'lows_stocks':[], 'like':[], 'comments':[]
    }
# Displaying on UI
def display_on_ui():
    all_stocks=models.Stocks.query.all()
    
    for data in all_stocks:
        data['stocks_name'].append(data.stocks_name)
        data['symbols'].append(data.stocks_name)
        
        data['high_stocks'].append(data.stocks_name)
        data['lows_stocks'].append(data.stocks_name)
        
        data['like'].append(data.stocks_name)
        data['comments'].append(data.stocks_name)
    
    SOCKET_IO.emit()
    return 
    
    
    
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
