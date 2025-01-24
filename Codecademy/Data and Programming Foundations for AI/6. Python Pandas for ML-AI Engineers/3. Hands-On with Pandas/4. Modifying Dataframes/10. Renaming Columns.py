"""
When we get our data from other sources, we often want to change the column names. For example, we might want all of the column names to follow variable name rules, so that we can use df.column_name (which tab-completes) rather than df['column_name'] (which takes up extra space).

You can change all of the column names at once by setting the 
Preview: Docs Loading link description
.columns
 property to a different list. This is great when you need to change all of the column names at once, but be careful! You can easily mislabel columns if you get the ordering wrong. Here’s an example:

df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']


This command edits the existing 
Preview: Docs Loading link description
DataFrame
 df.

Instructions
Checkpoint 1 Enabled
1.
The DataFrame df contains data about movies from IMDb.

We want to present this data to some film producers. Right now, our column names are in lower case, and are not very descriptive. Let’s modify df using the .columns attribute to make the following changes to the columns:

Old	New
id	ID
name	Title
genre	Category
year	Year Released
imdb_rating	Rating
"""
import codecademylib3
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)