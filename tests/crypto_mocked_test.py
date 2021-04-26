'''
    crypto_mocked_test.py
    Tests to see if crypto function will print out correct responses to valid
    names and errors.
'''
import unittest
import sys
import os

#sys.path.append(os.path.abspath("../../")) for when in unmocked folder
sys.path.append(os.path.abspath('../'))
from stock import Stock

DATA_INPUT = "input"
EXPECTED_OUTPUT = "expected"

class CryptoTestCase(unittest.TestCase):
    """
    Crypto search test case class.
    """
    def setUp(self):
        self.success_test_params = [
            {
                DATA_INPUT: '', #default test
                EXPECTED_OUTPUT: [
                    {
                        'symbol': 'crypto1',
                        'price': '0.292'
                    },
                    {
                        'symbol': 'crypto2',
                        'price': '0.292'
                    },
                    {
                        'symbol': 'crypto3',
                        'price': '0.292'
                    },
                    {
                        'symbol': 'crypto4',
                        'price': '0.292'
                    }
                ]
            },
            {
                DATA_INPUT: 'CTXCUSDT', #search test
                EXPECTED_OUTPUT: [{'symbol' : 'CTXCUSDT', 'price' : '0.111'}]
            },
            {
                DATA_INPUT: 'wer2sdvv', #error test
                EXPECTED_OUTPUT: {'wer2sdvv' : 'Not Found'}
            }
        ]

    def test_crypto(self):
        """
        Tests to see if crypto method will return dictionary with
        correct info or error message.
        """
        test_pass = 1
        for test in self.success_test_params:
            test_crypto = Stock()

            actual_result = test_crypto.crypto(test[DATA_INPUT])
            expected_result = test[EXPECTED_OUTPUT]
            self.assertEqual(len(actual_result), len(expected_result)) #Same Length
            if len(expected_result) == 1 and isinstance(expected_result, dict):
                t_input = test[DATA_INPUT]
                self.assertEqual(actual_result[t_input], expected_result[t_input])
            else:
                for i in range(len(actual_result)):
                    self.assertEqual(len(actual_result[i]), len(expected_result[i]))
                    self.assertEqual(
                        isinstance(actual_result[i]['price'], str),
                        isinstance(expected_result[i]['price'], str)
                        )
            print("TEST{} passed".format(test_pass))
            test_pass += 1
        print("All test cases pass")


if __name__ == '__main__':
    unittest.main()
