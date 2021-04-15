import json

def parse_api_data(data):
    ''' Parse stock data retrieved from the API '''
    parsed_data = {}
    for category_dict in data:
        parsed_data.update(category_dict)
    
    stocks_data = {'allStocks': []}
    for category in ['Mega', 'Tech', 'Energy', 'Utilities', 'Finance']:
        for symbol in parsed_data[category].keys():
            stocks_data['allStocks'].append(parsed_data[category][symbol])

    return stocks_data