'''
Congratulations - being able to identify variable types is the first (and most important) step towards working with data. The next is understanding how Python (and the pandas library) store your data.

When you read a data file (such as a csv) with pandas, 
Preview: Docs Python is a strongly typed language. At runtime, it prevents typing errors and engages in little implicit type conversion.
data types
 are assigned to each column. Pandas does its best to predict what kind of data type each variable should contain. For example, if a column contains only integer values, it will be stored as an int32 or int64. This usually works, but problems can arise for our analysis later on when there’s a mismatch between the real-world variable type and the data type pandas assigns.

With numerical 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
, pandas expects any column that has decimal values to be a float and anything without decimal values to be an integer. If any non-numeric characters appear in the column, pandas will treat it as an object.

It’s possible to determine the data types of the columns in your DataFrame with the .dtypes attribute.

For example, in our cereal dataset, Pandas returned the following list:

print(cereal.dtypes)

Copy to Clipboard

name	object
id	int64
name	object
mfr	object
type	object
fiber	float64
rating	float64
shelf	object
vitamins	int64
coupons	int64
price	float64
dtype: object	
Best practices for data storage say that we should match the data type of the column with its real-world variable type. Therefore:

Continuous (numerical) variables should usually be stored as the float data type because they allow us to store decimal values.

Discrete (numerical) variables should be stored as the int datatype to represent mathematically that they are discrete.

(note that the difference between int32/int64 and float32/float64 does not concern us here – it is an issue for much larger numbers)

Using float and int to store quantitative variables is important so that you can later perform numerical operations on those values. It also helps indicate what the variables refer to in the real world. Keeping them separate helps ensure that we perform the right calculations and get the right results. For example,

If a variable appears with the wrong data type, we can change it with the .astype() function.

cereal['id'] = cereal['id'].astype("string")

print(cereal.dtypes)

Copy to Clipboard

name	object
id	string
name	object
mfr	object
type	object
fiber	float64
rating	float64
shelf	object
vitamins	int64
coupons	int64
price	float64
dtype: object	
The .astype() function can be used to convert between a numerical data types, including:

int32 int64
float32 float64
object
string
bool
However, some data types require all values to be filled in. For example, you cannot convert between a float and an int if there are any null values.

Let’s go ahead and 
Preview: Docs Loading link description
try
 to clean up our Netflix data.

Instructions
Checkpoint 1 Passed
1.
Run the code in the workspace to view the first five rows of the movies dataframe.

Checkpoint 2 Enabled
2.
Check the data types of all the numerical variables in the movies DataFrame with .dtypes. Make sure to print the data types to the console.

Are there any mismatches between data types and variable types?

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Try to change the cast_count variable to an integer of type int64.

This will cause an error - that is OK! We expect there to be an error here. As long as the check mark on the left of the screen turns green, you’ve done it correctly.

If we didn’t check for null values in advance, this error message might be the first time we find out that we have null values.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Turns out we have to fill in the missing values. We actually don’t have a good way to know how many people are in each movie, so we will fill in the missing values with 0. We know that no movie has zero cast members, so this will logically be very odd, but will allow us to preserve the integrity of the data while converting the values.

First, uncomment the line of code that replaces the null values with 0. (movies['cast_count'].fillna(0, inplace = True)) Note that it is above the line of code you just wrote.

Then, re-run the code.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
Now check the data types again and be sure they match what you expected.

'''

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types
print(movies.dtypes)

# Fill in the missing cast_count values with 0
movies['cast_count'].fillna(0, inplace = True)

# Change the type of the cast_count column
movies['cast_count'] = movies['cast_count'].astype("int64")

# Check the data types of the columns again. 
print(movies.dtypes)