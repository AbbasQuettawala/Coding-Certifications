'''
In this lesson we discussed several ways of examining an association between two quantitative 
Preview: Docs Loading link description
variables
. More specifically, we:

Used scatter plots to examine relationships between quantitative variables
Used covariance and correlation to quantify the strength of a linear relationship between two quantitative variables
Note that the dataset used in this lesson was downloaded from kaggle.

Instructions
As a final exercise, a new dataset named penguins has been uploaded for you in script.py. This dataset contains various measurements for a sample of penguins. To practice the skills learned in this lesson, here are some things to try:

Inspect the first few rows of data.
Create a scatter plot of flipper length (flipper_length_mm) and body mass (body_mass_g).
Inspect your plot. What is the relationship between these variables?
Calculate the covariance for these two variables.
Calculate the correlation for these two variables. Does this number make sense given the plot you created?
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3
from scipy.stats import pearsonr
np.set_printoptions(suppress=True, precision = 1) 

penguins = pd.read_csv('penguins.csv')

#print the first few rows
print(penguins.head())

#create a scatter plot
plt.scatter(penguins.flipper_length_mm, penguins.body_mass_g)
plt.show()

#calculate covariance:
covariance_mat = np.cov(penguins.flipper_length_mm, penguins.body_mass_g)
print("covariance matrix: ")
print(covariance_mat)

print("covariance: ", covariance_mat[1][0])

#calculate correlation:
correlation, p = pearsonr(penguins.flipper_length_mm, penguins.body_mass_g)
print("correlation: ", correlation)