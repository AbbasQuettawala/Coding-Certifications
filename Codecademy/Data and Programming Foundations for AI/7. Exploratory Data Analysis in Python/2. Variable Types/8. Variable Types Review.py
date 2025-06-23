'''
Variable Types Review
11 min
You’ve done a fantastic job! In this lesson, you have:

Discovered the different types of 
Preview: Docs Loading link description
variables
 you will encounter when working with data and their corresponding 
Preview: Docs Loading link description
data types
 in Python.
Explored datasets with 
Preview: Docs Sends a HEAD request to a web server and it returns a response object.
.head()
.
Assessed categories within variables with the .unique() method.
Practiced ways to check the data type of variables like the .dtypes attribute.
Altered data with the .fillna() method.
Learned how to change the data types of variables using the .astype() method.
Investigated the pandas category data type.
Developed your One-Hot Encoding skills with the pd.get_dummies() method.
In this lesson, we used a cereal dataset from Kaggle , which was originally created by Chris Crawford and which contains data on various cereal brands in the US. We made alterations to this data for the purposes of the lesson. The other datasets used in this lesson can be found here:

The movies dataset courtesy of Shivam Bansal via Kaggle.
The auto dataset courtesy of UCI Machine Learning Repository.
The titanic dataset courtesy of Khashayar Baghizadeh Hosseini via Kaggle.
The clothes dataset courtesy of Nicapotato via Kaggle.
Let’s practice the skills you just learned. Because this is review, we won’t check your work on these tasks. If you get an error, take a look at the hints or go back to that exercise in this lesson and review how to do it.

Instructions
Return the first 10 rows of the auto dataframe.

Return the data types of the auto dataframe with the .dtypes attribute.

Change the price category from int to float with the .astype() method, then recheck the data types with .dtypes.

Convert the engine_size variable to the category data type with an order of [‘small’, ‘medium’, ‘large’], and check the order with the .unique() method.

Create a new variable called engine_codes which contains the numerical codes associated with each category in the engine_size variable with the .cat.codes accessor. Check the new values with the .head() method.

One-Hot Encode the body-style category in the auto dataframe. Then check the dataframe with .head().
'''

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
auto = pd.read_csv('autos.csv', index_col=0)

# Print the first 10 rows of the auto dataset
print(auto.head(10))

# Print the data types of the auto dataframe
print(auto.dtypes)

# Change the data type of price to float
auto['price'] = auto['price'].astype('float')

# Set the engine_size data type to category
auto['engine_size'] = pd.Categorical(auto['engine_size'],
['small','medium','large'], ordered=True)

# Create the engine_codes variable by encoding engine_size
auto['engine_codes'] = auto['engine_size'].cat.codes
print(auto.head())


# One-Hot Encode the body-style variable
auto = pd.get_dummies(auto, columns = ['body-style'])
# Check the order of the type column
print(auto.dtypes)

