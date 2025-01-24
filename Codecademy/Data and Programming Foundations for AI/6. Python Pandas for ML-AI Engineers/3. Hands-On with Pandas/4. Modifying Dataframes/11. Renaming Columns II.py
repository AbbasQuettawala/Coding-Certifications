"""
You also can rename individual columns by using the .rename method. Pass a dictionary like the one below to the columns keyword argument:

{'old_column_name1': 'new_column_name1', 'old_column_name2': 'new_column_name2'}


Here’s an example:

df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)


The code above will rename name to First Name and age to Age.

Using rename with only the columns keyword will create a new 
Preview: Docs Loading link description
DataFrame
, leaving your original DataFrame unchanged. That’s why we also passed in the keyword argument inplace=True. Using inplace=True lets us edit the original DataFrame.

There are several reasons why .rename is preferable to 
Preview: Docs Loading link description
.columns
:

You can rename just one column
You can be specific about which column names are getting changed (with .column you can accidentally switch column names if you’re not careful)
Note: If you misspell one of the original column names, this command won’t fail. It just won’t change anything.

Instructions
Checkpoint 1 Enabled
1.
If we didn’t know that df was a table of movie ratings, the column name might be confusing.

To clarify, let’s rename name to movie_title.

Use the keyword inplace=True so that you modify df rather than creating a new DataFrame!
"""
import codecademylib3
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns = {
  'name': 'movie_title'
},
   inplace=True)
print(df)