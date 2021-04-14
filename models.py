from app import DB


# This is User table 
class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username=DB.Column(DB.String(80),unique=True, nullable=False)
    bio= DB.Column(DB.Text(), nullable=False)
    stocks= DB.relationship('like_table',backref='owner',lazy= 'select')
    
# user like stocks table
class like_table(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    stcks= DB.Column(DB.Integer,DB.ForeignKey('user.id'))
    all_stock= DB.relationship('Stocks',backref= 'stocks',lazy= 'select')

# All the Stocks Table
class Stocks(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    stocks_name = DB.Column(DB.String(80),unique=True, nullable=False)
    symbols = DB.Column(DB.String(10), unique=True, nullable=False)
    high_stocks = DB.Column(DB.Integer, nullable=False)
    low_stocks = DB.Column(DB.Integer, nullable=False)
    likes= DB.Column(DB.Integer, nullable=False)
    comment = DB.Column(DB.Text(), nullable=False)
    stocks_column = DB.Column(DB.Integer,DB.ForeignKey('like_table.id'))
    
# All the comments Table   
class Comments(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    stocks_name = DB.Column(DB.String(80), unique=True, nullable=False)
    symbols = DB.Column(DB.String(10), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    high_stocks = DB.Column(DB.Integer, nullable=False)
    low_stocks = DB.Column(DB.Integer, nullable=False)
    likes=DB.Column(DB.Integer, nullable=False)
    comment = DB.Column(DB.Text(), nullable=False)
    
