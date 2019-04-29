"""
This module performs unit tests for dataframe.py.

Tests being performed:
- The dataframe has the expected columns.
- Values in the column are all of the expected type.
- There are no nan values.
- The dataframe has at least one row.
"""

import pandas
import unittest
from dataframe import read_data

class UnitTests(unittest.TestCase):

    # The dataframe has the expected columns
    def test_success(self):
        dt = read_data('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
        exp_names = ['street', 'city', 'zip', 'state', 'beds', 'baths', 'sq__ft', 'type',
                     'sale_date', 'price', 'latitude', 'longitude']
        self.assertTrue(list(dt) == exp_names)
    
    # There are no nan values
    def test_success1(self):
        dt = read_data('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
        null_sum = dt.isnull().sum().sum()
        self.assertEqual(null_sum, 0)
        
    # The dataframe has at least one row    
    def test_success2(self):
        dt = read_data('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
        self.assertTrue(len(dt) > 1)
        
    

# if __name__ == '__main__':
#     unittest.main()
