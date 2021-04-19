''' Utility functions for handling Stock API data '''

def parse_api_data(data):
    ''' Parse stock data retrieved from the API '''

    stocks_data = {'allStocks': []}

    if len(data) != 1:
        parsed_data = {}
        for category_dict in data:
            parsed_data.update(category_dict)

        for category in ['Mega', 'Tech', 'Energy', 'Utilities', 'Finance']:
            for symbol in parsed_data[category].keys():
                stocks_data['allStocks'].append(parsed_data[category][symbol])
    else:
        company = list(data.keys())[0]
        stocks_data['allStocks'].append(data[company])

    return stocks_data
