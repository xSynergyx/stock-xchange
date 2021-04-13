'''
    news_unittest.py
    Tests to see if values are accurate depending on desired search of stock and to check
    if apis switch after 10 requests in a minute.
'''
import unittest
import sys
import os

#sys.path.append(os.path.abspath("../../")) for when in unmocked folder
sys.path.append(os.path.abspath('../'))
from stock import Stock

DATA_INPUT = "input"
EXPECTED_OUTPUT = "expected"

class NewsTestCase(unittest.TestCase):
    """
    Stock search test case class.
    """
    def setUp(self):
        self.success_test_params = [
            {
                DATA_INPUT: ['AAPL']*12, #NYT TO IEX TEST after 12 requests
                EXPECTED_OUTPUT: ['a', 'b', 'c', 'd', 'e']
            },
            { 
                DATA_INPUT: ['MSFT'],
                EXPECTED_OUTPUT: ['a', 'b', 'c', 'd', 'e']
            }

        ]

    def test_news(self):
        """
        Tests to see if search method returns a dictionary with the correct
        information based on the submitted stock symbols
        """
        test_pass = 1
        for test in self.success_test_params:
            test_stock = Stock()
            #do for loop
            
            actual_result = None
            lst_symbols = test[DATA_INPUT]
            
            for symb in lst_symbols:
                actual_result = test_stock.news(symb)
            expected_result = test[EXPECTED_OUTPUT]
            self.assertEqual(len(actual_result), len(expected_result)) #Same Length
            for i in range(len(actual_result)): 
                self.assertEqual(actual_result[i] is str, expected_result[i] is str)
            print("TEST{} passed".format(test_pass))
            test_pass += 1
        print("All test cases pass")


if __name__ == '__main__':
    unittest.main()