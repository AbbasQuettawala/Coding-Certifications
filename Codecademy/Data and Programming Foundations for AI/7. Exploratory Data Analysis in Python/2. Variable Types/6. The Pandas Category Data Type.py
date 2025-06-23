'''
For ordinal categorical 
Preview: Docs Loading link description
variables
, we often want to store two different pieces of information: category labels and their order. None of the 
Preview: Docs Python is a strongly typed language. At runtime, it prevents typing errors and engages in little implicit type conversion.
data types
 we’ve covered so far can store both of these at once.

For example, let’s take another look at the shelf variable in our cereal DataFrame, which contains the shelf each item is on stored as 
Preview: Docs A string is a sequence of characters contained within a pair of single quotes or double quotes.
strings
. We can use the .unique() method to inspect the category names:

print(cereal['shelf'].unique())

Copy to Clipboard

# Output
[top, mid, bottom]

Copy to Clipboard

At this point, Python does not know that these categories have an inherent order. Luckily, there is a specific data type for categorical variables in pandas called category to address this problem! The pandas .Categorical() method can be used to store data as type category and indicate the order of the categories.

cereal['shelf'] = pd.Categorical(cereal['shelf'], ['bottom', 'mid', 'top'], ordered=True)

Copy to Clipboard

Now, not only does Python recognize that the shelf column is an ordinal variable, it understands that top > mid > bottom. If we call .unique() on this column again, we see how Python retains the correct rankings.

print(cereal['shelf'].unique())

Copy to Clipboard

# Output
[bottom, mid, top]
Categories (6, object): [bottom < mid < top]

Copy to Clipboard

This is helpful in the event that we would like to sort the column by category; if we use .sort_values(), the DataFrame will be sorted by the logical order of the shelf column as opposed to the alphabetical order.

Instructions
Checkpoint 1 Passed
1.
Run the code in the workspace to print the first five rows of the movies DataFrame along with the unique values of the rating column.

Checkpoint 2 Passed
2.
Change the data type of the rating variable to categorical. Set an order of [‘NR’, ‘G’ , ‘PG’, ‘PG-13’, ‘R’].

Checkpoint 3 Passed
3.
Check the new order of the categories with .unique(). Make sure to print the output.
'''

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
movies = pd.read_csv('netflix_movies.csv')

# View the first five rows of the dataframe
print(movies.head())

# Print the unique values of the rating column
print(movies['rating'].unique())

# Change the data type of `rating` to category
movies['rating'] = pd.Categorical(movies['rating'], ['PG-13', 'R', 'PG', 'G', 'NR'], ordered=True)

# Recheck the values of `rating` with .unique()
print(movies['rating'].unique())
