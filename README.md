# Homework 3-4: Coding style and Unit tests.

##### Final grade: 14/14  
  
Grade: 7/14   

-2: In using_functions.test_create_dataframe: instead of having the if ... else pass structure, it is better to have an if...elif...elif... structure. This way, your code will be more succint.   
-2: In using_functions: using a count to test conditions technically works, but that in general is considered bad style, because numbers inheritantly are not meant for this kind of condition checking and we have boolean variables for those.   
-1: In using_functions: In general you shouldn't return magic strings such as "None" and then use that for condition checking.   
-2: In test_dataframe.py: Test names should be descriptive.

------

**Note: This homework has a total of 14 points.**

In this homework, you will create two python modules and put them in PEP8 style.

1. Function code (5 points). Last week you wrote python codes that read an online file and created a data frame that has at least 3 columns. Now: (a) create a python module ``dataframe.py`` that reads the data in homework 2;  and (b) ``dataframpe.py`` should generate an ValueError execption if the dataframe doesn't have the expected column names.

1. Test code (5 points). Create a python file ``test_dataframe.py`` that has unit tests for dataframe.py. Include at least 2 of the following tests:

   - You have the expected columns.
   - Values in the column are all of the expected type.
   - There are no nan values.
   - The dataframe has at least one row.
   
1. Coding style (4 points). Make all codes PEP8 compliant and provide the output from pylint to demonstrate that you have accomplished this.
