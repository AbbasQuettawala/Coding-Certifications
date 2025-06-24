'''
While summary statistics are certainly helpful for exploring and quantifying a feature, we might find it hard to wrap our minds around a bunch of numbers. This is why data visualization is such a powerful element of EDA.

For quantitative 
Preview: Docs Loading link description
variables
, boxplots and histograms are two common visualizations. These plots are useful because they simultaneously communicate information about minimum and maximum values, central location, and spread. Histograms can additionally illuminate patterns that can impact an analysis (e.g., skew or multimodality).

Python’s seaborn library, built on top of matplotlib, offers the boxplot() and histplot() 
Preview: Docs Functions allow tasks to be performed multiple times within a program without having to be rewritten.
functions
 to easily plot data from a pandas DataFrame:

import matplotlib.pyplot as plt 
import seaborn as sns

# Boxplot for rent
sns.boxplot(x='rent', data=rentals)
plt.show()
plt.close()

Copy to Clipboard

boxplot of rent

# Histogram for rent
sns.histplot(x='rent', data=rentals)
plt.show()
plt.close()

Copy to Clipboard

histogram of rent

Instructions
Checkpoint 1 Passed
1.
Using the movies DataFrame, create a boxplot for production_budget using the boxplot() function from seaborn. Don’t forget to display the plot using plt.show() and close the plot using plt.close().

Checkpoint 2 Passed
2.
Create a histogram for production_budget using the histplot() function from seaborn.

From the plots, what do you notice about the distribution of movie budgets?

Both plots show that the distribution of movie budgets is skewed to the right, with some outlier movies having extremely high budgets. This is consistent with the high mean budget value we saw earlier, since the mean is affected by skewness and outliers.
'''


import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv('movies.csv')

# Create a boxplot for movie budget 
sns.boxplot(x='production_budget', data=movies)
plt.show()
plt.close()

# Create a histogram for movie budget
sns.histplot(x='production_budget', data=movies)
plt.show()
plt.close
