'''
Beyond visualizing relationships, we can also use summary statistics to quantify the strength of certain associations. Covariance is a summary statistic that describes the strength of a linear relationship. A linear relationship is one where a straight line would best describe the pattern of points in a scatter plot.

Covariance can range from negative infinity to positive infinity. A positive covariance indicates that a larger value of one variable is associated with a larger value of the other. A negative covariance indicates a larger value of one variable is associated with a smaller value of the other. A covariance of 0 indicates no linear relationship. Here are some examples:

This figure shows three different plots. In the first, the points are almost exactly along a line with a positive slope and the label is "large positive covariance". In the middle plot, the points are randomly scattered and the label is "covariance of zero". In the last plot, the points are almost exactly on a negatively sloping line and the label is "large negative covariance"

To calculate covariance, we can use the cov() function from NumPy, which produces a covariance matrix for two or more 
Preview: Docs Loading link description
variables
. A covariance matrix for two variables looks something like this:

variable 1	variable 2
variable 1	variance(variable 1)	covariance
variable 2	covariance	variance(variable 2)
In python, we can calculate this matrix as follows:

cov_mat_price_sqfeet = np.cov(housing.price, housing.sqfeet)
print(cov_mat_price_sqfeet)
#output: 
[[184332.9  57336.2]
 [ 57336.2 122045.2]]

Copy to Clipboard

Notice that the covariance appears twice in this matrix and is equal to 57336.2.

Instructions
Checkpoint 1 Passed
1.
Use the cov() function from NumPy to calculate the covariance matrix for the sqfeet variable and the beds variable. Save the covariance matrix as cov_mat_sqfeet_beds

Checkpoint 2 Passed
2.
Print out the value stored in the variable cov_mat_sqfeet_beds.

Checkpoint 3 Passed
3.
Look at the covariance matrix you just printed and find the covariance of sqfeet and beds. Save that number as a variable named cov_sqfeet_beds.
'''


import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision = 1) 

housing = pd.read_csv('housing_sample.csv')

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.sqfeet, housing.beds)
print(cov_mat_sqfeet_beds)

# store the covariance as cov_sqfeet_beds
cov_sqfeet_beds =  228.2