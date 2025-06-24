'''
When it comes to categorical 
Preview: Docs Loading link description
variables
, the measures of central tendency and spread that worked for describing numeric variables, like mean and standard deviation, generally becomes unsuitable when we’re dealing with discrete values. Unlike numbers, categorical values are not continuous and oftentimes do not have an intrinsic ordering.

Instead, a good way to summarize categorical variables is to generate a frequency table containing the count of each distinct value. For example, we may be interested to know how many of the New York City rental listings are from each borough. Related, we can also find which borough has the most listings.

The pandas library offers the .value_counts() method for generating the counts of all values in a DataFrame column:

# Counts of rental listings in each borough
df.borough.value_counts()

Copy to Clipboard

Output:

Manhattan    3539
Brooklyn     1013
Queens        448
By default, it returns the results sorted in descending order by count, where the top element is the mode, or the most frequently appearing value. In this case, the mode is Manhattan with 3,539 rental listings.

Instructions
Checkpoint 1 Passed
1.
Using the movies DataFrame, find the number of movies in each genre and save the counts to a variable called genre_counts. Print genre_counts to see the result.
'''

import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the counts to genre_counts
genre_counts = movies.genre.value_counts()
print(genre_counts)
