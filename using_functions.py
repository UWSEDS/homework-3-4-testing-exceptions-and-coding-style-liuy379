"""
1. Find an on-line data source (e.g., from data.gov). Write python codes that
read the on-line file and create a data frame that has at least 3 columns.

2. Create the function test_create_dataframe that takes a pandas DataFrame as
input and returns True if the following conditions hold:
- The DataFrame contains only the columns that you specified in #1.
- The columns contain the correct data type
- There are at least 10 rows in the DataFrame.
"""

import pandas as pd
trans = pd.read_csv('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
exp_names = ['street', 'city', 'zip', 'state', 'beds', 'baths', 'sq__ft', 'type',
             'sale_date', 'price', 'latitude', 'longitude']
exp_names_sorted = sorted(exp_names)

def sort_dict(x):
    target = {}
    for key in sorted(x.keys()):
        target[key] = x[key].name
    return target

exp_dtypes = trans.dtypes
exp_dtypes_sorted = sort_dict(exp_dtypes)


def test_create_dataframe(df):
    act_names = list(df)
    act_names_sorted = sorted(act_names)

    act_dtypes = df.dtypes
    act_dtypes_sorted = sort_dict(act_dtypes)

    count = 0
    if act_names_sorted == exp_names_sorted:
        count += 1
    else:
        pass
    
    if act_dtypes_sorted == exp_dtypes_sorted:
        count += 1
    else: 
        pass
    
    if len(df) >= 10:
        count += 1
    else:
        pass
    
    if count == 3:
        return True
    else:
        return False

def output_file():
    if test_create_dataframe(trans):
        return trans
    else:
        return "None"














