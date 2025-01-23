"""
You can also add data using lists.

For example, you can pass in a list of lists, where each one represents a row of data. Use the keyword argument columns to pass a list of column names.

df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])


This command produces a DataFrame df2 that looks like this:

name	address	age
John Smith	123 Main St.	34
Jane Doe	456 Maple Ave.	28
Joe Schmo	789 Broadway	51

In this example, we were able to control the ordering of the columns because we used lists.

Instructions
Checkpoint 1 Enabled
1.
You’re running a chain of pita shops called Pita Power. You want to create a DataFrame with information on your different store locations.

Use a list of lists to create a DataFrame with the following data:

Store ID	Location	Number of Employees
1	San Diego	100
2	Los Angeles	120
3	San Francisco	90
4	Sacramento	115

We have filled in the information for the first two rows in df2.

Add the code to create the 3rd and 4th rows, and the column names.
"""
import codecademylib3
import pandas as pd

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4

  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=['Store ID', 'Location', 'Number of Employees'
    #add column names here
  ])

print(df2)