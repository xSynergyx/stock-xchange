import os
from flask import Flask, send_from_directory, request
import json

app = Flask(__name__, static_folder='./build/static')


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

@app.route('/stocks', methods = ['GET'])
def stocks():
    # With the actual data, we would query an SQLAlchemy model
    # for all records and convert the result to JSON. Haven't looked much
    # into converting SQLAlchemy query results to JSON, but it should be
    # straight forward

    # This method of searching a hardcoded JSON file is just for testing.

    stocks_data = {}
    with open('test_stock_data.json', 'r') as json_file:
        stocks_data = json.loads(json_file.read())

    return stocks_data

@app.route('/stock_page', methods = ['POST'])
def stock_page():
    # Get the stock id sent from the client side
    stock_id = int(request.get_json()['stock_id'])
    page_data = {}

    # Server would query a SQLAlchemy model for the database record 
    # matching the passed in stock_id. Then, the resulting stock info data
    # would be translated to JSON format and sent back to the client. 
    # This method of searching a hardcoded JSON file is just for testing.
    stock_data = {}
    with open('test_stock_data.json', 'r') as json_file:
        stocks_data = json.loads(json_file.read())['allStocks']
        for stock in stocks_data:
            if stock['id'] == stock_id:
                stock_data = stock
                break

    with open('test_stock_page.json', 'r') as json_file:
        page_data = json.loads(json_file.read())

    return {"stock_data": stock_data, "page_data": page_data}

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)
