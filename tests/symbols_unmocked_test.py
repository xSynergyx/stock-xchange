'''
    symbols_unmocked_test.py
    Tests to see if symbols function will recognize a csv file and if it will print out
    correct data.
'''
import unittest
import sys
import os

#sys.path.append(os.path.abspath("../../")) for when in unmocked folder
sys.path.append(os.path.abspath('../'))
from stock import symbols

DATA_INPUT = "input"
EXPECTED_OUTPUT = "expected"

class SymbolsTestCase(unittest.TestCase):
    """
    Stock search test case class.
    """
    def setUp(self):
        self.success_test_params = [
            {
                DATA_INPUT: 'test1.csv',
                EXPECTED_OUTPUT: ['SS1', 'S2', '3', 'SSS4']
            },
            {
                DATA_INPUT: 'notExist.csv',
                EXPECTED_OUTPUT: ['File Not Found']
            },
            {
                DATA_INPUT: 'error.csv',
                EXPECTED_OUTPUT: ['Wrong Format']
            }
        ]

    def test_symbols(self):
        """
        Symbol function tests.
        """
        test_pass = 1
        for test in self.success_test_params:
            actual_result = symbols(test[DATA_INPUT])
            expected_result = test[EXPECTED_OUTPUT]
            self.assertEqual(len(actual_result), len(expected_result)) #Same Length
            if len(actual_result) != 1:
                for i in range(4):
                    self.assertEqual(len(actual_result[i]) <= 4, len(expected_result[i]) <= 4)
            else:
                self.assertEqual(actual_result, expected_result)
            print("TEST{} passed".format(test_pass))
            test_pass += 1
        print("All test cases pass")


if __name__ == '__main__':
    unittest.main()
