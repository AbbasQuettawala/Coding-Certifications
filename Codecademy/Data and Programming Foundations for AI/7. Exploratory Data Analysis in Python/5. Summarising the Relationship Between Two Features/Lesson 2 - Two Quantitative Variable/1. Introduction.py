'''
When associations exist between 
Preview: Docs Loading link description
variables
, it means that information about the value of one variable gives us information about the value of the other variable. In this lesson, we will cover ways of examining an association between two quantitative variables.

Throughout the next few exercises, we’ll examine some data about Texas housing rentals on Craigslist — an online classifieds site. The data dictionary is as follows:

price: monthly rental price in U.S.D.
type: type of housing (eg., 'apartment', 'house', 'condo', etc.)
sqfeet: housing area, in square feet
beds: number of beds
baths: number of baths
lat: latitude
long: longitude
Except for type, all of these variables are quantitative. Which pairs of variables do you think might be associated? For example, does knowing something about price give you any information about square footage?

Instructions
Checkpoint 1 Passed
1.
The dataset described above has been saved for you as a pandas dataframe named housing. Use the .head() method to print the first 10 rows and inspect some more of the data. What are some other quantitative variables that might be related to each other?
'''

import pandas as pd
import codecademylib3


housing = pd.read_csv('housing_sample.csv')

#print the first 10 rows of data:
print(housing.head(10))