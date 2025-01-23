"""
A DataFrame is an object that stores data as rows and columns. You can think of a DataFrame as a spreadsheet or as a SQL table. You can manually create a DataFrame or fill it with data from a CSV, an Excel spreadsheet, or a SQL query.

DataFrames have rows and columns. Each column has a name, which is a string. Each row has an index, which is an integer. DataFrames can contain many different data types: strings, ints, floats, tuples, etc.

You can pass in a dictionary to pd.DataFrame(). Each key is a column name and each value is a list of column values. The columns must all be the same length or you will get an error. Here’s an example:

df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})


This command creates a DataFrame called df1 that looks like this:

name	address	age
John Smith	123 Main St.	34
Jane Doe	456 Maple Ave.	28
Joe Schmo	789 Broadway	51
Instructions
Checkpoint 1 Enabled
1.
You run an online clothing store called Panda’s Wardrobe. You need a DataFrame containing information about your products.

Create a DataFrame with the following data that your inventory manager sent you:

Product ID	Product Name	Color
1	t-shirt	blue
2	t-shirt	green
3	skirt	red
4	skirt	black

We have already filled in the information for Product ID in df1.

Add the code to create the columns Product Name and Color and their associated data.
"""

import codecademylib3
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)