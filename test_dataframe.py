"""
This module performs unit tests for dataframe.py.

Tests being performed:
- The dataframe has the expected columns.
- Values in the column are all of the expected type.
- There are no nan values.
- The dataframe has at least one row.
"""

import unittest
from dataframe import read_data

class UnitTests(unittest.TestCase):
    """ Testcases for dataframe.py """
    def test_success(self):
        """ The dataframe has the expected columns """
        target = read_data('http://samplecsvs.s3.amazonaws.com/'
                           'Sacramentorealestatetransactions.csv')
        exp_names = ['street', 'city', 'zip', 'state', 'beds', 'baths', 'sq__ft', 'type',
                     'sale_date', 'price', 'latitude', 'longitude']
        self.assertTrue(list(target) == exp_names)
    def test_success1(self):
        """ There are no nan values """
        target = read_data('http://samplecsvs.s3.amazonaws.com/'
                           'Sacramentorealestatetransactions.csv')
        null_sum = target.isnull().sum().sum()
        self.assertEqual(null_sum, 0)
    def test_success2(self):
        """ The dataframe has at least one row """
        target = read_data('http://samplecsvs.s3.amazonaws.com/'
                           'Sacramentorealestatetransactions.csv')
        self.assertTrue(len(target) > 1)

if __name__ == '__main__':
    unittest.main()
