'''' Database for User information and Stocks '''
from database import DB


# This is User table
class Person(DB.Model):
    ''' Users name and liked stocks with Bio '''
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(120), unique=True, nullable=False)
    bio = DB.Column(DB.Text(), nullable=True)
    all_stockstocks = DB.relationship('Liketable',
                                      backref='person',
                                      lazy='dynamic')

    def __init__(self, username, bio):
        self.username = username
        self.bio = bio

    def __repr__(self):
        return '<Person %r>' % self.id


# user like stocks table
class Liketable(DB.Model):
    ''' User like stocks table'''
    id = DB.Column(DB.Integer, primary_key=True)
    person_id = DB.Column(DB.Integer,
                          DB.ForeignKey('person.id'),
                          nullable=False)
    stocks = DB.Column(DB.String(80), nullable=True)
    all_stock = DB.relationship('Stocks', backref='liketable', lazy='dynamic')

    def __init__(self, stocks, person):
        self.stocks = stocks
        self.person_id = person

    def __repr__(self):
        return '<Liketable %r>' % self.id


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
    all_stock = DB.relationship('Comments', backref='owner', lazy='dynamic')

    def __init__(self, stocks_name, symbols, high_stocks, low_stocks,
                 current_price, likes, category):
        self.stocks_name = stocks_name
        self.symbols = symbols
        self.high_stocks = high_stocks
        self.low_stocks = low_stocks
        self.current_price = current_price
        self.likes = likes
        self.category = category

    def __repr__(self):
        return '<Stocks %r>' % self.id


# Cryptocurrency Table
class Crypto(DB.Model):
    '''Cryptocurrency'''
    id = DB.Column(DB.Integer, primary_key=True)
    symbols = DB.Column(DB.String(10), unique=True, nullable=True)
    current_price = DB.Column(DB.Float, nullable=True)
    likes = DB.Column(DB.Integer, nullable=True)
    category = DB.Column(DB.String(80), nullable=True)
    def __init__(self, symbols, current_price, likes, category):

        self.symbols = symbols
        self.current_price = current_price
        self.likes = likes
        self.category = category

    def __repr__(self):
        return '<Crypto %r>' % self.id


# All the comments Table
class Comments(DB.Model):
    ''' All the comment Table'''
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(120), nullable=False)
    comment = DB.Column(DB.Text(), nullable=False)
    stocks_column = DB.Column(DB.Integer, DB.ForeignKey('stocks.id'))

    def __init__(self, username, comment, owner):
        self.username = username
        self.comment = comment
        self.stocks_column = owner

    def __repr__(self):
        return '<Comments %r>' % self.id
