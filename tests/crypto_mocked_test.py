'''
    crypto_mocked_test.py
    Tests to see if crypto function will print out correct responses to valid
    names and errors.
'''
import unittest
import sys
import os
from stock import Stock

#sys.path.append(os.path.abspath("../../")) for when in unmocked folder
sys.path.append(os.path.abspath('../'))

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
                EXPECTED_OUTPUT: {
                    'crypto1':
                        {
                            'Symbol': 'crypto1',
                            'Price': '0.292',
                            'Category': 'Cryptocurrency'
                        },
                    'crypto2':
                        {
                            'Symbol': 'crypto2',
                            'Price': '0.292',
                            'Category': 'Cryptocurrency'
                        },
                    'crytpo3':
                        {
                            'Symbol': 'crypto3',
                            'Price': '0.292',
                            'Category': 'Cryptocurrency'
                        },
                    'crypto4':
                        {
                            'Symbol': 'crypto4',
                            'Price': '0.292',
                            'Category': 'Cryptocurrency'
                        }
                }
            },
            {
                DATA_INPUT: 'CTXCUSDT', #search test
                EXPECTED_OUTPUT: {
                    'Symbol': 'CTXCUSDT',
                    'Price': '0.111', 
                    'Category': 'Cryptocurrency'
                }
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
            if len(actual_result) == 1 and isinstance(actual_result, dict): #Error check
                t_input = test[DATA_INPUT]
                self.assertEqual(actual_result[t_input], expected_result[t_input])
            elif len(actual_result) == 4 and isinstance(actual_result, dict): #Default Search Check
                for i, j in zip(actual_result, expected_result):
                    print(actual_result[i])
                    self.assertEqual(len(actual_result[i]), len(expected_result[j]))
                    self.assertEqual(
                        isinstance(actual_result[i]['Price'], str),
                        isinstance(expected_result[j]['Price'], str)
                        )
            elif len(actual_result) == 3 and isinstance(actual_result, dict):#Normal search
                self.assertEqual(
                    isinstance(actual_result['Price'], str),
                    isinstance(expected_result['Price'], str)
                )
            else:
                assert False, "Test failed"
            print("TEST{} passed".format(test_pass))
            test_pass += 1
        print("All test cases pass")


if __name__ == '__main__':
    unittest.main()
