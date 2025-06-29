'''
Introduction
7 min
Before diving into formal analysis with a dataset, it is often helpful to perform some initial investigations of the data through exploratory data analysis (EDA) to get a better sense of what you will be working with. Basic summary statistics and visualizations are important components of EDA as they allow us to condense a large amount of information into a small set of numbers or graphics that can be easily interpreted.

This lesson focuses on univariate summaries, where we explore each variable separately. This is useful for answering questions about each individual feature. 
Preview: Docs Loading link description
Variables
 can typically be classified as quantitative (i.e., numeric) or categorical (i.e., discrete). Depending on its type, we may want to choose different summary metrics and visuals to use.

Let’s say we have the following dataset on New York City rental listings imported into a pandas DataFrame (subsetted from the StreetEasy dataset):

import pandas as pd

# Import dataset
rentals = pd.read_csv('streeteasy.csv')

# Preview first 5 rows
print(rentals.head())

Copy to Clipboard

rent	size_sqft	borough
2550	480	Manhattan
11500	2000	Manhattan
3000	1000	Queens
4500	916	Manhattan
4795	975	Manhattan
As seen, we have two quantitative variables (rent and size_sqft) and one categorical variable (borough). The pandas library offers a handy method .describe() for displaying some of the most common summary statistics for the columns in a DataFrame. By default, the result only includes numeric columns, but we can specify include='all' to the method to display categorical ones as well:

# Display summary statistics for all columns
print(rentals.describe(include='all'))

Copy to Clipboard

rent	size_sqft	borough
count	5000.000000	5000.000000	5000
unique	NaN	NaN	3
top	NaN	NaN	Manhattan
freq	NaN	NaN	3539
mean	4536.920800	920.101400	NaN
std	2929.838953	440.150464	NaN
min	1250.000000	250.000000	NaN
25%	2750.000000	633.000000	NaN
50%	3600.000000	800.000000	NaN
75%	5200.000000	1094.000000	NaN
max	20000.000000	4800.000000	NaN
This is a great way to get an overview of all the variables in a dataset. Notice how different statistics are displayed depending on the variable type. In the rest of the lesson, we’ll look more closely at the common ways to summarize and visualize quantitative and categorical variables.

Instructions
Checkpoint 1 Passed
1.
In script.py, we’ve imported a dataset containing information on the budget and earnings of movies from various genres into a DataFrame called movies.

Start by inspecting the first 5 rows of movies using the .head() method and print the result.

How many quantitative and categorical variables do you see?

Checkpoint 2 Passed
2.
Use the .describe() method to display the summary statistics for movies and print the result. Make sure to show statistics for all columns in the DataFrame.

What kinds of metrics are displayed for quantitative columns versus categorical columns?
'''


import codecademylib3
import pandas as pd

movies = pd.read_csv('movies.csv')

# Print the first 5 rows 
print(movies.head())

# Print the summary statistics for all columns
print(movies.describe(include='all'))