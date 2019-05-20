"""
(a) create a python module dataframe.py that reads the data in homework 2
(b) dataframpe.py should generate an ValueError execption if the dataframe doesn't
    have the expected column names
"""

from using_functions import output_file

def read_data():
    """ this function reads data into a dataframe """
    target = output_file()
    exp_names = ['street', 'city', 'zip', 'state', 'beds', 'baths', 'sq__ft', 'type',
                 'sale_date', 'price', 'latitude', 'longitude']
    if list(target) == exp_names:
        pass
    else:
        raise "Dataframe doesn't have the expected column names."
    return target
