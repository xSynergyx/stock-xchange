from app import DB


class Stocks(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    stocks_name = DB.Column(DB.String(80), unique=True, nullable=False)
    symbols = DB.Column(DB.String(10), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    high_stocks = DB.Column(DB.Integer, nullable=False)
    low_stocks = DB.Column(DB.Integer, nullable=False)
    comment = DB.Column(DB.Text(), nullable=False)
    
    

    # def __repr__(self):
    #     return '<Stocks %r>' % self.username
    def __init__(self,stocks_name,symbols,high_stocks,low_stocks,comments):
        self.stocksname=stocks_name
        self.symbols=symbols
        self.high_stocks=high_stocks
        self.low_stocks=low_stocks
        self.comment=comments