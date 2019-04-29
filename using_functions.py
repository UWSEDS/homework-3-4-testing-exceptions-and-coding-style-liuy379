"""
1. Find an on-line data source (e.g., from data.gov). Write python codes that
read the on-line file and create a data frame that has at least 3 columns.

2. Create the function test_create_dataframe that takes a pandas DataFrame as
input and returns True if the following conditions hold:
- The DataFrame contains only the columns that you specified in #1.
- The columns contain the correct data type
- There are at least 10 rows in the DataFrame.

import pandas as pd
trans = pd.read_csv('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
"""


def test_create_dataframe(df):
    if (df.columns.equals(trans.columns) and
        df.dtypes.equals(trans.dtypes) and
        len(df) >= 10):
        return True
    else:
        return False
