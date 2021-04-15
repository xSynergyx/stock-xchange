'''' Database for User information and Stocks '''
from app import DB
# This is User table
class Person(DB.Model):
    ''' Users name and liked stocks with Bio '''
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    bio = DB.Column(DB.Text(), nullable=False)
    stocks = DB.relationship('like_table', backref='user')

    def __init__(self, username, bio):
        self.username = username
        self.bio = bio

# user like stocks table
class Liketable(DB.Model):
    ''' User like stocks table'''
    id = DB.Column(DB.Integer, DB.ForeignKey('person.id'), primary_key=True)
    # stocks = DB.Column(DB.Integer, DB.ForeignKey('person.id'))
    all_stock = DB.relationship('Stocks', backref='stocks', lazy='select')

    def __init__(self, stocks):
        self.stocks = stocks


# All the Stocks Table
class Stocks(DB.Model):
    '''all the Stocks from the API'''
    id = DB.Column(DB.Integer, primary_key=True)
    stocks_name = DB.Column(DB.String(80), unique=True, nullable=False)
    symbols = DB.Column(DB.String(10), unique=True, nullable=False)
    high_stocks = DB.Column(DB.Integer, nullable=False)
    low_stocks = DB.Column(DB.Integer, nullable=False)
    likes = DB.Column(DB.Integer, nullable=False)
    category= DB.Column(DB.String(80), unique=True, nullable=False)

    # stocks_column = DB.Column(DB.Integer,DB.ForeignKey('like_table.id'))
    all_stock = DB.relationship('Comments', backref='comments', lazy='select')

    def __init__(self, stocks_name, symbols, high_stocks, low_stocks, likes, category):
        self.stocks_name = stocks_name
        self.symbols = symbols
        self.high_stocks = high_stocks
        self.low_stocks = low_stocks
        self.comment = likes
        self.category = category

# All the comments Table
class Comments(DB.Model):
    ''' All the comment Table'''
    id = DB.Column(DB.Integer,DB.ForeignKey('stocks.id'), primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    comment = DB.Column(DB.Text(), nullable=False)
    # stocks_column = DB.Column(DB.Integer, DB.ForeignKey('stocks.id'))

    def __init__(self, username, comment):
        self.username = username
        self.comment = comment
