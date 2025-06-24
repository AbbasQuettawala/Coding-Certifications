'''
For quantitative 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
, we often want to describe the central tendency, or the “typical” value of a variable. For example, what is the typical cost of rent in New York City?

There are several common measures of central tendency:

Mean: The average value of the variable, calculated as the sum of all values divided by the number of values.
Median: The middle value of the variable when sorted.
Mode: The most frequent value of the variable.
Trimmed mean: The mean excluding x percent of the lowest and highest data points.
For our rentals DataFrame with a column named rent that contains rental prices, we can calculate the central tendency statistics listed above as follows:

# Mean
rentals.rent.mean()

# Median
rentals.rent.median()

# Mode
rentals.rent.mode()

# Trimmed mean
from scipy.stats import trim_mean
trim_mean(rentals.rent, proportiontocut=0.1)  # trim extreme 10%

Copy to Clipboard

Instructions
Checkpoint 1 Passed
1.
Using the same movies DataFrame from the last exercise, find the mean production_budget for all movies and save it to a variable called mean_budget. Print mean_budget to see the result.

Checkpoint 2 Passed
2.
Save the median budget to a variable called med_budget and print the result.

Checkpoint 3 Passed
3.
Save the mode to a variable called mode_budget and print the result.

How do the mean, median, and mode of movie budgets compare to each other?

Checkpoint 4 Passed
4.
Find the mean of the budget after removing 20% of the lowest and highest data points. Save the trimmed mean to a variable called trmean_budget and print the result.

How does trimming the most extreme data points affect the mean budget?
'''


import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the mean to mean_budget
mean_budget = movies.production_budget.mean()
print(mean_budget)

# Save the median to med_budget
med_budget = movies.production_budget.median()
print(med_budget)

# Save the mode to mode_budget
mode_budget = movies.production_budget.mode()
print(mode_budget)


# Save the trimmed mean to trmean_budget
from scipy.stats import trim_mean
trmean_budget = trim_mean(movies.production_budget, proportiontocut = 0.2)
print(trmean_budget)