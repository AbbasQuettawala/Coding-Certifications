'''
One of the best ways to quickly visualize the relationship between quantitative 
Preview: Docs Loading link description
variables
 is to plot them against each other in a scatter plot. This makes it easy to look for patterns or trends in the data. Let’s start by plotting the area of a rental against its monthly price to see if we can spot any patterns.

plt.scatter(x = housing.price, y = housing.sqfeet)
plt.xlabel('Rental Price (USD)')
plt.ylabel('Area (Square Feet)')
plt.show()

Copy to Clipboard

This image shows a scatter plot with price on the x-axis and area on the y-axis. There is a clear linear relationship; rentals that cost more tend to have larger area.

While there’s a lot of variation in the data, it seems like more expensive housing tends to come with slightly more space. This suggests an association between these two variables.

It’s important to note that different kinds of associations can lead to different patterns in a scatter plot. For example, the following plot shows the relationship between the age of a child in months and their weight in pounds. We can see that older children tend to weigh more but that the growth rate starts leveling off after 36 months:

Plot showing the relationship between the age of a child in months and their weight in pounds. We can see that older children tend to weigh more but that the growth rate starts leveling off after 36 months

If we don’t see any patterns in a scatter plot, we can probably guess that the variables are not associated. For example, a scatter plot like this would suggest no association:

Scatter plot with no apparent pattern; the points appear randomly distributed.

Instructions
Checkpoint 1 Passed
1.
The housing data has been saved for you as a dataframe named housing in script.py. Create a scatter plot to see if there is an association between the number of bedrooms (beds) and the area (sqfeet) of a rental. Use Number of Bedrooms for the x-axis of your scatter plot. Do you think these variables are associated? If so, is the relationship what you expected?
'''


import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.xlabel('Beds')
plt.ylabel('Sqfeet')

plt.show()