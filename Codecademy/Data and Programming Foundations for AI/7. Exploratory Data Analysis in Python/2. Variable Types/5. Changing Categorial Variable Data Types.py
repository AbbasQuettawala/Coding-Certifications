'''
Now let’s focus on Categorical 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
 and make sure they are in the correct format. Let’s take another look at the cereal dataset to assess the 
Preview: Docs Python is a strongly typed language. At runtime, it prevents typing errors and engages in little implicit type conversion.
data types
 of our categorical variables.

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
Just like with numerical variables, best practices for categorical data storage say that we should match the data type of the column with its real-world variable type. However, the types are a little more nuanced:

Nominal variables are often represented by the object data type. Columns in the object data type can contain any combination of values, including strings, integers, booleans, etc. This means that string operations like 
Preview: Docs Loading link description
.lower()
 are not possible on object columns.

Nominal variables are also represented by the string data type. However, Pandas usually guesses object rather than string, so if you want a column to be a string, you will likely have to explicitly tell pandas to make it a string. This is most important if you want to do string manipulations on a column like .lower().

Ordinal variables should be represented as objects, but pandas often guesses int since they are often encoded as whole numbers.

Binary variables can be represented as bool, but pandas often guesses int or object data types.

We have a lot to change in our cereal dataset, so let’s go through them one by one.

We already learned about the .astype() function and can be used to convert into the following categorical data types:

object
string
bool
We’ll start by looking at the data types again.

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
id should be an object since it’s a nominal variable that is not a string.
name and mfr should be strings since they are words and we may want to lowercase, uppercase, or otherwise transform them with string methods.
shelf and type can stay as objects since they are codes (though it would be just as valid to make them into strings)
cereal['id'] = cereal['id'].astype("object")
cereal['name'] = cereal['name'].astype("string")
cereal['mfr'] = cereal['mfr'].astype("string")

Copy to Clipboard

name	object
id	object
name	string
mfr	string
type	object
fiber	float64
rating	float64
shelf	object
vitamins	int64
coupons	int64
price	float64
dtype: object	
Now it’s time for you to 
Preview: Docs Loading link description
try
 it on the Netflix data. Be sure to take into account how the data is recorded and what you might want to do with each variable.
'''

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types of dataframe 
print(movies.dtypes)

# Add the variables you plan to change to this list
change = ['title', 'rating', 'duration']

# Change the title variable to a "string"
movies['title'] = movies['title'].astype('string')
movies['rating'] = movies['rating'].astype('int32')

# Change any other variables

# Print the data types again
print(movies.dtypes)