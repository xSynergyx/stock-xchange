'''' Database for User information and Stocks '''
from database import DB

# This is User table
class Person(DB.Model):
    ''' Users name and liked stocks with Bio '''
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    bio = DB.Column(DB.Text(), nullable=False)
    stocks = DB.relationship('Liketable', backref='person', lazy='select')

    def __init__(self, username, bio):
        self.username = username
        self.bio = bio

# user like stocks table
class Liketable(DB.Model):
    ''' User like stocks table'''
    id = DB.Column(DB.Integer, primary_key=True)
    person_id = DB.Column(DB.Integer, DB.ForeignKey('person.id'), nullable=False)
    all_stock = DB.relationship('Stocks', backref='liketable', lazy='select')

    def __init__(self, stocks):
        self.stocks = stocks


# All the Stocks Table
class Stocks(DB.Model):
    '''all the Stocks from the API'''
    id = DB.Column(DB.Integer, primary_key=True)
    stocks_name = DB.Column(DB.String(80), nullable=True)
    symbols = DB.Column(DB.String(10), unique=True, nullable=True)
    high_stocks = DB.Column(DB.Float, nullable=True)
    low_stocks = DB.Column(DB.Float, nullable=True)
    current_price = DB.Column(DB.Float, nullable=True)
    likes = DB.Column(DB.Integer, nullable=True)
    category = DB.Column(DB.String(80), nullable=True)

    like_table_id = DB.Column(DB.Integer, DB.ForeignKey('liketable.id'))
    all_stock = DB.relationship('Comments', backref='stocks', lazy='select')

    def __init__(self, stocks_name, symbols, high_stocks,
                 low_stocks, current_price, likes, category):
        self.stocks_name = stocks_name
        self.symbols = symbols
        self.high_stocks = high_stocks
        self.low_stocks = low_stocks
        self.current_price = current_price
        self.likes = likes
        self.category = category

# All the comments Table
class Comments(DB.Model):
    ''' All the comment Table'''
    id = DB.Column(DB.Integer, DB.ForeignKey('stocks.id'), primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    comment = DB.Column(DB.Text(), nullable=False)
    # stocks_column = DB.Column(DB.Integer, DB.ForeignKey('stocks.id'))

    def __init__(self, username, comment):
        self.username = username
        self.comment = comment
