"""
(a) create a python module dataframe.py that reads the data in homework 2
(b) dataframpe.py should generate an ValueError execption if the dataframe doesn't have the expected column names
'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
"""

import pandas as pd

def read_data(url):
    dt = pd.read_csv(url)
    exp_names = ['street', 'city', 'zip', 'state', 'beds', 'baths', 'sq__ft', 'type',
             'sale_date', 'price', 'latitude', 'longitude']
    
    if list(dt) == exp_names:
        pass
    else:
        raise ValueError("Dataframe doesn't have the expected column names")
    
    return dt