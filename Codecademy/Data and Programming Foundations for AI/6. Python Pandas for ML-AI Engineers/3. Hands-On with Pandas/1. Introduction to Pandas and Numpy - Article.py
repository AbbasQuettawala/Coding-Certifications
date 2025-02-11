"""
pandas and NumPy are very useful libraries in Python. Let’s learn how to use them!

Pandas
Pandas is a very popular library for working with data (its goal is to be the most powerful and flexible open-source tool, and in our opinion, it has reached that goal). DataFrames are at the center of pandas. A DataFrame is structured like a table or spreadsheet. The rows and the columns both have indexes, and you can perform operations on rows or columns separately.

A pandas DataFrame can be easily changed and manipulated. Pandas has helpful functions for handling missing data, performing operations on columns and rows, and transforming data. If that wasn’t enough, a lot of SQL functions have counterparts in pandas, such as join, merge, filter by, and group by. With all of these powerful tools, it should come as no surprise that pandas is very popular among data scientists.

NumPy
NumPy is an open-source Python library that facilitates efficient numerical operations on large quantities of data. There are a few functions that exist in NumPy that we use on pandas DataFrames. For us, the most important part about NumPy is that pandas is built on top of it. So, NumPy is a dependency of Pandas.

Installation
If you have Anaconda installed, NumPy and pandas may have been auto-installed as well! If they haven’t been, or if you want to update to the latest versions, you can open a terminal window and run the following commands:

conda install numpy
conda install pandas

If you don’t have Anaconda installed, you can alternatively install the libraries using pip by running the following commands from your terminal:

pip install numpy
pip install pandas

Once you’ve installed these libraries, you’re ready to open any Python coding environment (we recommend Jupyter Notebook). Before you can use these libraries, you’ll need to import them using the following lines of code. We’ll use the abbreviations np and pd, respectively, to simplify our function calls in the future.

import numpy as np
import pandas as pd

NumPy Arrays
NumPy arrays are unique in that they are more flexible than normal Python lists. They are called ndarrays since they can have any number (n) of dimensions (d). They hold a collection of items of any one data type and can be either a vector (one-dimensional) or a matrix (multi-dimensional). NumPy arrays allow for fast element access and efficient data manipulation.

The code below initializes a Python list named list1:

list1 = [1,2,3,4]

To convert this to a one-dimensional ndarray with one row and four columns, we can use the np.array() function:

array1 = np.array(list1)
print(array1)

Output:

[1 2 3 4]
To get a two-dimensional ndarray from a list, we must start with a Python list of lists:

list2 = [[1,2,3],[4,5,6]]
array2 = np.array(list2)
print(array2)

Output:

[[1 2 3]
 [4 5 6]]
In the above output, you may notice that the NumPy array print-out is displayed in a way that clearly demonstrates its multi-dimensional structure: two rows and three columns.

Many operations can be performed on NumPy arrays which makes them very helpful for manipulating data:

Selecting array elements

Slicing arrays

Reshaping arrays

Splitting arrays

Combining arrays

Numerical operations (min, max, mean, etc)

Mathematical operations can be performed on all values in a ndarray at one time rather than having to loop through values, as is necessary with a Python list. This is very helpful in many scenarios. Say you own a toy store and decide to decrease the price of all toys by €2 for a weekend sale. With the toy prices stored in an ndarray, you can easily facilitate this operation.

toyPrices = np.array([5,8,3,6])
print(toyPrices - 2)

Output:

[3 6 1 4]
If, however, you had stored your toy prices in a Python list, you would have to manually loop through the entire list to decrease each toy price.

toyPrices = [5,8,3,6]
# print(toyPrices - 2) -- Not possible. Causes an error
for i in range(len(toyPrices)):
    toyPrices[i] -= 2
print(toyPrices)

Output:

[3,6,1,4]
Pandas Series and Dataframes
Just as the ndarray is the foundation of the NumPy library, the Series is the core object of the pandas library. A pandas Series is very similar to a one-dimensional NumPy array, but it has additional functionality that allows values in the Series to be indexed using labels. A NumPy array does not have the flexibility to do this. This labeling is useful when you are storing pieces of data that have other data associated with them. Say you want to store the ages of students in an online course to eventually figure out the average student age. If stored in a NumPy array, you could only access these ages with the internal ndarray indices 0,1,2.... With a Series object, the indices of values are set to 0,1,2... by default, but you can customize the indices to be other values such as student names so an age can be accessed using a name. Customized indices of a Series are established by sending values into the Series constructor, as you will see below.

A Series holds items of any one data type and can be created by sending in a scalar value, Python list, dictionary, or ndarray as a parameter to the pandas Series constructor. If a dictionary is sent in, the keys may be used as the indices.

# Create a Series using a NumPy array of ages with the default numerical indices
ages = np.array([13,25,19])
series1 = pd.Series(ages)
print(series1)

Output:

0  |  13
1  |  25
2  |  19
dtype: int64
When printing a Series, the data type of its elements is also printed. To customize the indices of a Series object, use the index argument of the Series constructor.

# Create a Series using a NumPy array of ages but customize the indices to be the names that correspond to each age
ages = np.array([13,25,19])
series1 = pd.Series(ages,index=['Emma', 'Swetha', 'Serajh'])
print(series1)

Output:

Emma    |  13
Swetha  |  25
Serajh  |  19
dtype: int64
Series objects provide more information than NumPy arrays do. Printing a NumPy array of ages does not print the indices or allow us to customize them.

ages = np.array([13,25,19])
print(ages)

Output:

[13 25 19]
Another important type of object in the pandas library is the DataFrame. This object is similar in form to a matrix as it consists of rows and columns. Both rows and columns can be indexed with integers or String names. One DataFrame can contain many different types of data types, but within a column, everything has to be the same data type. A column of a DataFrame is essentially a Series. All columns must have the same number of elements (rows).

There are different ways to fill a DataFrame such as with a CSV file, a SQL query, a Python list, or a dictionary. Here we have created a DataFrame using a Python list of lists. Each nested list represents the data in one row of the DataFrame. We use the keyword columns to pass in the list of our custom column names.

dataf = pd.DataFrame([
    ['John Smith','123 Main St',34],
    ['Jane Doe', '456 Maple Ave',28],
    ['Joe Schmo', '789 Broadway',51]
    ],
    columns=['name','address','age'])

This is how the DataFrame is displayed:

          name      |   address     |   age
0    | John Smith   | 123 Main St   |   34
1    | Jane Doe     | 456 Maple Ave |   28
2    | Joe Schmo    | 789 Broadway  |   51
The default row indices are 0,1,2..., but these can be changed. For example, they can be set to be the elements in one of the columns of the DataFrame. To use the names column as indices instead of the default numerical values, we can run the following command on our DataFrame:

dataf.set_index('name')

Output:

   name      |   address     |  age
John Smith   | 123 Main St   |   34
Jane Doe     | 456 Maple Ave |   28
Joe Schmo    | 789 Broadway  |   51
DataFrames are useful because they make it much easier to select, manipulate, and summarize data. Their tabular format (a table with rows and columns) also makes it easier to label, simpler to read, and easier to export data to and from a spreadsheet. Understanding the power of these new data structures is the key to unlocking many new avenues for data manipulation, exploration, and analysis!
"""