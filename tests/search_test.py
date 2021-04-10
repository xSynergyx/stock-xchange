'''
    stock_unittest.py
    Tests to see if values are accurate depending on desired search of stock based on
    symbol.
'''
import unittest
import sys
import os

sys.path.append(os.path.abspath("../../"))
from stock.Stock import search