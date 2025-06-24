'''
For categorical 
Preview: Docs Loading link description
variables
, bar charts and pie charts are common options for visualizing the count (or proportion) of values in each category. They can also convey the relative frequencies of each category.

Python’s seaborn library offers several 
Preview: Docs Loading link description
functions
 that can create bar charts. The simplest for plotting the counts is countplot():

# Bar chart for borough
sns.countplot(x='borough', data=rentals)
plt.show()
plt.close()

Copy to Clipboard

Bar chart of borough

There are currently no functions in the seaborn library for creating a pie chart, but the pandas library provides a convenient wrapper function around matplotlib‘s pie() function that can generate a pie chart from any column in a DataFrame:

# Pie chart for borough
rentals.borough.value_counts().plot.pie()
plt.show()
plt.close()

Copy to Clipboard

Pie chart of borough

In general, many data analysts avoid pie charts because people are better at visually comparing areas of rectangles than wedges of a pie. For a variable with a small number of categories (i.e., fewer than three), a pie chart is a reasonable choice; however, for more complex data, a bar chart is usually preferable.

Instructions
Checkpoint 1 Passed
1.
Using the movies DataFrame, create a bar chart for genre using the countplot() function from seaborn. Don’t forget to display the plot using plt.show() and close the plot using plt.close().

Checkpoint 2 Passed
2.
Create a pie chart for genre using the .pie() method from pandas.

From the plots, what do you notice about the relative frequencies of movie genres?
'''

import codecademylib3
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

movies = pd.read_csv('movies.csv')

# Create a bar chart for movie genre 
sns.countplot(x='genre', data=movies)
plt.show()
plt.close()

# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.show()
plt.close()
