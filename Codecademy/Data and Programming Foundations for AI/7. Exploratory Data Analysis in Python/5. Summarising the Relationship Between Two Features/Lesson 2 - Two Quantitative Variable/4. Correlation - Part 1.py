'''
Like covariance, Pearson Correlation (often referred to simply as “correlation”) is a scaled form of covariance. It also measures the strength of a linear relationship, but ranges from -1 to +1, making it more interpretable.

Highly associated 
Preview: Docs Loading link description
variables
 with a positive linear relationship will have a correlation close to 1. Highly associated variables with a negative linear relationship will have a correlation close to -1. Variables that do not have a linear association (or a linear association with a slope of zero) will have correlations close to 0.

This figure shows 5 different plots. From left to right, the plots show a correlation of 1, a large positive correlation, no correlation, a large negative correlation, and a correlation of -1.)

The pearsonr() function from scipy.stats can be used to calculate correlation as follows:

from scipy.stats import pearsonr
corr_price_sqfeet, p = pearsonr(housing.price, housing.sqfeet)
print(corr_price_sqfeet) #output: 0.507

Copy to Clipboard

Generally, a correlation larger than about .3 indicates a linear association. A correlation greater than about .6 suggestions a strong linear association.

Instructions
Checkpoint 1 Passed
1.
Use the pearsonr function from scipy.stats to calculate the correlation between sqfeet and beds. Store the result in a variable named corr_sqfeet_beds and print out the result. How strong is the linear association between these variables?

Checkpoint 2 Passed
2.
Generate a scatter plot of beds and sqfeet again. Does the correlation value make sense?
'''

import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

housing = pd.read_csv('housing_sample.csv')

# calculate corr_sqfeet_beds and print it out:
corr_sqfeet_beds, p = pearsonr(housing.sqfeet, housing.beds)
print(corr_sqfeet_beds)

plt.xlabel('Number of beds')
plt.ylabel('Number of sqfeet')
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.show()



# create the scatter plot here:
