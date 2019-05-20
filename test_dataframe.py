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
    def test_column_names(self):
        """ The dataframe has the expected columns """
        target = read_data()
        exp_names = ['street', 'city', 'zip', 'state', 'beds', 'baths', 'sq__ft', 'type',
                     'sale_date', 'price', 'latitude', 'longitude']
        self.assertTrue(sorted(list(target)) == sorted(exp_names))
    def test_nan_values(self):
        """ There are no nan values """
        target = read_data()
        null_sum = target.isnull().sum().sum()
        self.assertEqual(null_sum, 0)
    def test_least_row_counts(self):
        """ The dataframe has at least one row """
        target = read_data()
        self.assertTrue(len(target) > 1)

if __name__ == '__main__':
    unittest.main()
