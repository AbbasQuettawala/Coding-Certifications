"""
Now that we have our data saved into an easy-to-work-with format, let’s investigate it.

We’ll use Python’s pandas library, which is designed for working with data (and will quickly become familiar to you). Start by importing the library and using the read_csv() function to read the CSV data into a DataFrame object:

import pandas
 
census_df = pandas.read_csv("census.csv")

Copy to Clipboard

By default, the first row of the CSV file is read in as the header row. We can use the 
Preview: Docs Loading link description
.head()
 method to preview the first few rows of the DataFrame.

Sometimes columns have ambiguous or confusing names (like Census codes). We might also want to rename those columns. We can use the .columns attribute to rename the column headings if needed:

# Preview DataFrame
print(census_df.head())
 
# Rename DataFrame columns
census_df.columns = ['name', 'total_commuters', 'state']

Copy to Clipboard

The pandas library offers a lot more functionality for exploring and manipulating tabular data, but that is out of 
Preview: Docs Loading link description
scope
 for this lesson. You can learn more in our Learn Data Analysis with Pandas course.

Instructions
Checkpoint 1 Enabled
1.
Start by importing the pandas library.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Create a variable called commute_df. Set your variable to be a pandas DataFrame from the commute_data.csv file you created in the last exercise.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Preview the first few rows of commute_df using the .head() method and print out the output.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Notice how the column headings for commute_df show the codes the Census uses. That’s not very intuitive!

Rename the headings to more descriptive names, then print the first few rows of the DataFrame again to see the changes.

Congratulations!!! Not only have you used Python to get data, but you’ve also modified a dataset programmatically!! You are well on your way to becoming a Data Scientist!
"""
import pandas as pd


commute_df = pd.read_csv('commute_data.csv')

print(commute_df.head())

commute_df.columns = ['county_name', 'total_commuters', 'super_commuters', 'state_code', 'county_code']

print(commute_df.head())
