'''
The spread of a quantitative variable describes the amount of variability. This is important because it provides context for measures of central tendency. For example, if there is a lot of variability in New York City rent prices, we can be less certain that the mean or median price is representative of what the typical rent is.

There are several common measures of spread:

Range: The difference between the maximum and minimum values of a variable.
Interquartile range (IQR): The difference between the 75th and 25th percentile values.
Variance: The average of the squared distance from each data point to the mean.
Standard deviation (SD): The square root of the variance.
Mean absolute deviation (MAD): The mean absolute value of the distance between each data point and the mean.
For our rentals DataFrame, we can calculate the spread for the rent column as follows:

# Range
rentals.rent.max() - rentals.rent.min()

# Interquartile range
rentals.rent.quantile(0.75) - rentals.rent.quantile(0.25)

from scipy.stats import iqr
iqr(rentals.rent)  # alternative way

# Variance
rentals.rent.var()

# Standard deviation
rentals.rent.std()

# Mean absolute deviation
rentals.rent.mad()

Copy to Clipboard

Instructions
Checkpoint 1 Passed
1.
Using the movies DataFrame, find the range for production_budget and save it to a variable called range_budget. Print range_budget to see the result.

Checkpoint 2 Passed
2.
Save the interquartile range for budget to a variable called iqr_budget and print the result.

Checkpoint 3 Passed
3.
Save the variance to a variable called var_budget and print the result.

Checkpoint 4 Passed
4.
Save the standard deviation to a variable called std_budget and print the result.

Checkpoint 5 Passed
5.
Save the mean absolute deviation to a variable called mad_budget and print the result.
'''


import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the range to range_budget
range_budget = movies.production_budget.max() - movies.production_budget.min()
print(range_budget)

# Save the interquartile range to iqr_budget
iqr_budget = movies.production_budget.quantile(0.75) - movies.production_budget.quantile(0.25)
print(iqr_budget)

# Save the variance to var_budget
var_budget = movies.production_budget.var()
print(var_budget)

# Save the standard deviation to std_budget
std_budget = movies.production_budget.std()
print(std_budget)

# Save the mean absolute deviation to mad_budget
mad_budget = movies.production_budget.mad()
print(mad_budget)
