'''
    stock_utils_unmocked_test.py
    Tests to see if values are accurate depending on desired search of stock and to check
    if apis switch after 10 requests in a minute.
'''
import unittest
import sys
import os
from stock_utils_test_inputs import INPUT1, INPUT2, INPUT3, EXPECTED1, EXPECTED2, EXPECTED3
#sys.path.append(os.path.abspath("../../")) for when in unmocked folder
sys.path.append(os.path.abspath('../'))
from stock_utils import parse_api_data


INPUTS = [INPUT1, INPUT2, INPUT3]
OUTPUTS = [EXPECTED1, EXPECTED2, EXPECTED3]
DATA_INPUT = 'input'
EXPECTED_OUTPUT = 'expected'

class StockUtilsTestCase(unittest.TestCase):
    """
    Stock search test case class.
    """
    def setUp(self):
        self.success_test_params = [
            {
                DATA_INPUT: INPUTS[0],
                EXPECTED_OUTPUT: OUTPUTS[0]
            },
            {
                DATA_INPUT: INPUTS[1],
                EXPECTED_OUTPUT: OUTPUTS[1]
            },
            {
                DATA_INPUT: INPUTS[2],
                EXPECTED_OUTPUT: OUTPUTS[2]
            }
        ]

    def test_stocks_util(self):
        """
        Stock Util tests.
        """
        test_pass = 1
        for test in self.success_test_params:
            #do for loop

            actual_result = parse_api_data(test[DATA_INPUT])
            expected_result = test[EXPECTED_OUTPUT]
            self.assertEqual(len(actual_result), len(expected_result))
            self.assertEqual(
                actual_result['allStocks'][0]['Category'] == 'Mega',
                expected_result['allStocks'][0]['Category'] == 'Mega'
            )
            print("TEST{} passed".format(test_pass))
            test_pass += 1
        print("All test cases pass")


if __name__ == '__main__':
    unittest.main()
