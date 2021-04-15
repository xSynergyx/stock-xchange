'''
    app.py
    Server file.
'''

import os
from flask import Flask, send_from_directory,json, session
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
COR_S = CORS(APP, resources={r"/*": {"origins": "*"}})
SOCKET_IO = SocketIO(APP,
                     cors_allowed_origins="*",
                     json=json,
                     manage_session=False)

stocks_List={'stocks_name':[] , 'symbols': [], 'high_stocks':[], 'lows_stocks':[], 'like':[], 'comments':[]
    }
# Displaying on UI
def display_on_ui():
    
    print('this')
    return None
    
    
    
@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    """ index """
    return send_from_directory('./build', filename)

@SOCKET_IO.on('connect')
def on_connect():
    """ checks if user connected and dsiplay the leaderboard """
    print('User connected!')

@SOCKET_IO.on('disconnect')
def on_disconnect():
    """CHecks if user is disconnected """
    print('User disconnected!')


if __name__ == "__main__":
    # DB.create_all()
    # Note that we don't call APP.run anymore. We call SOCKET_IO.run with APP arg
    SOCKET_IO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
