'''
It’s important to note that there are some limitations to using correlation or covariance as a way of assessing whether there is an association between two 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
. Because correlation and covariance both measure the strength of linear relationships with non-zero slopes, but not other kinds of relationships, correlation can be misleading.

For example, the four scatter plots below all show pairs of variables with near-zero correlations. The bottom left image shows an example of a perfect linear association where the slope is zero (the line is horizontal). Meanwhile, the other three plots show non-linear relationships — if we drew a line through any of these 
Preview: Docs Loading link description
sets
 of points, that line would need to be curved, not straight!

This figure shows four different scatter plots where the correlation is equal to zero in every case. The bottom left image shows an example of a perfect linear association where the slope is zero (the line is horizontal). Meanwhile, the other three plots show non-linear relationships, where the points follow a curved pattern.

Instructions
Checkpoint 1 Passed
1.
A simulated dataset named sleep has been loaded for you in script.py. The hypothetical data contains two columns:

hours_sleep: the number of hours that a person slept
performance: that person’s performance score on a physical task the next day
Create a scatter plot of hours_sleep (on the x-axis) and performance (on the y-axis). What is the relationship between these variables?

Checkpoint 2 Passed
2.
Calculate the correlation for hours_sleep and performance and save the result as corr_sleep_performance. Then, print out corr_sleep_performance. Does the correlation accurately reflect the strength of the relationship between these variables?
'''


import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

sleep = pd.read_csv('sleep_performance.csv')

# create your scatter plot here:
plt.scatter(sleep.hours_sleep, sleep.performance)
plt.show()

# calculate the correlation for `hours_sleep` and `performance`:
corr_sleep_performance , p = pearsonr(sleep.hours_sleep, sleep.performance)
print(corr_sleep_performance)
