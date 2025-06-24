'''
A counts table is one approach for exploring categorical 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
, but sometimes it is useful to also look at the proportion of values in each category. For example, knowing that there are 3,539 rental listings in Manhattan is hard to interpret without any context about the counts in the other categories. On the other hand, knowing that Manhattan listings make up 71% of all New York City listings tells us a lot more about the relative frequency of this category.

We can calculate the proportion for each category by dividing its count by the total number of values for that variable:

# Proportions of rental listings in each borough
rentals.borough.value_counts() / len(rentals.borough)

Copy to Clipboard

Output:

Manhattan    0.7078
Brooklyn     0.2026
Queens       0.0896
Alternatively, we could also obtain the proportions by specifying normalize=True to the .value_counts() method:

df.borough.value_counts(normalize=True)

Copy to Clipboard

Instructions
Checkpoint 1 Passed
1.
Using the movies DataFrame, find the proportion of movies in each genre and save them to a variable called genre_props. Print genre_props to see the result.
'''


import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the proportions to genre_props
genre_props = movies.genre.value_counts(normalize=True)
print(genre_props)