"""
When we load a new 
Preview: Docs A DataFrame is the primary object used by Pandas to store and manipulate data.
DataFrame
 from a CSV, we want to know what it looks like.

If it’s a small DataFrame, you can display it by typing print(df).

If it’s a larger DataFrame, it’s helpful to be able to inspect a few items without having to look at the entire DataFrame.

The method .head() gives the first 5 rows of a DataFrame. If you want to see more rows, you can pass in the positional argument n. For example, df.head(10) would show the first 10 rows.

The method df.info() gives some statistics for each column.

Instructions
Checkpoint 1 Enabled
1.
You’re working for a Hollywood studio, trying to use data to predict the next big hit. Load the CSV imdb.csv into a variable called df, so that you can learn about popular movies from the past 90 years.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Let’s learn about these movies.

Paste the following code into script.py:

print(df.head())


What happens when you press “Run”?

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
What exactly is in this dataset?

Paste the following code into script.py to learn more about this data:

print(df.info())


What happens when you press “Run”?
"""

import codecademylib3
import pandas as pd
#load the CSV below:
df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())
