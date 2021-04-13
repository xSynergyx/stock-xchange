'''
    stock_unittest.py
    Tests to see if values are accurate depending on desired search of stock based on
    symbol.
'''
import unittest
import sys
import os

#sys.path.append(os.path.abspath("../../")) for when in unmocked folder
sys.path.append(os.path.abspath('../'))
from stock import Stock

DATA_INPUT = "input"
EXPECTED_OUTPUT = "expected"

class StockSearchTestCase(unittest.TestCase):
    """
    Stock search test case class.
    """
    def setUp(self):
        self.success_test_params = [
            {
                DATA_INPUT: ['XXXX'],
                EXPECTED_OUTPUT: {
                    'XXXX' : 'Not Found'
                }
            },
            {
                DATA_INPUT: ['AAPL'],
                EXPECTED_OUTPUT: {
                    'AAPL' :
                        {
                            'Symbol' : 'AAPL',
                            'Company' : 'Apple Inc',
                            'High' : 0,
                            'Low' : 0,
                            'Price' : 0
                        }
                }
            },
            {
                DATA_INPUT: ['JPM', 'JNJ'],
                EXPECTED_OUTPUT: {
                    'JPM':
                        {
                            'Symbol': 'JPM',
                            'Company': 'JPMorgan Chase & Co.',
                            'High': 0,
                            'Low': 0,
                            'Price': 0
                        },
                    'JNJ':
                        {
                            'Symbol': 'JNJ',
                            'Company': 'Johnson & Johnson',
                            'High': 0,
                            'Low': 0,
                            'Price': 0
                        }
                }
            },
            {
                DATA_INPUT: ['TOT', 'COP', 'EOG', 'TPL'],
                EXPECTED_OUTPUT: {
                    'TOT':
                        {
                            'Symbol': 'TOT',
                            'Company': 'Total SE - ADR',
                            'High': 0,
                            'Low': 0,
                            'Price': 0
                        },
                    'COP':
                        {
                            'Symbol': 'COP',
                            'Company': 'Conoco Phillips',
                            'High': 0,
                            'Low': 0,
                            'Price': 0
                        },
                    'EOG':
                        {
                            'Symbol': 'EOG',
                            'Company': 'EOG Resources, Inc.',
                            'High': 0,
                            'Low': 0,
                            'Price': 0
                        },
                    'TPL':
                        {
                            'Symbol': 'TPL',
                            'Company': 'Texas Pacific Land Corporation',
                            'High': 0,
                            'Low': 0,
                            'Price': 0
                        }
                }
            }
        ]

    def test_search(self):
        """
        Tests to see if search method returns a dictionary with the correct
        information based on the submitted stock symbols
        """
        test_pass = 1
        for test in self.success_test_params:
            test_stock = Stock()

            actual_result = test_stock.search(test[DATA_INPUT])
            expected_result = test[EXPECTED_OUTPUT]
            self.assertEqual(len(actual_result), len(expected_result)) #Same Length
            #Assuming this passed
            a_symbols = list(actual_result.keys())
            e_symbols = list(expected_result.keys())
            i = 0
            if type(expected_result[test[DATA_INPUT][0]]) == dict:
                while i < len(a_symbols):
                    a_symb = a_symbols[i] # actual symbol
                    e_symb = e_symbols[i] # expected symbol
                    self.assertEqual(
                        actual_result[a_symb]['Company'], expected_result[e_symb]['Company']
                    )
                    self.assertEqual(
                        actual_result[a_symb]['High'] is int, expected_result[e_symb]['High'] is int
                    )
                    i += 1
            else:
                self.assertEqual(actual_result, expected_result)
            print("TEST{} passed".format(test_pass))
            test_pass += 1
        print("All test cases pass")


if __name__ == '__main__':
    unittest.main()
