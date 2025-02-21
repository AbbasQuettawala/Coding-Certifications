"""
This lesson introduced some methods for combining multiple DataFrames:

Creating a 
Preview: Docs A DataFrame is the primary object used by Pandas to store and manipulate data.
DataFrame
 made by matching the common columns of two DataFrames is called a merge
We can specify which columns should be matches by using the keyword arguments left_on and right_on
We can combine DataFrames whose rows don’t all match using left, right, and outer merges and the how keyword argument
We can stack or concatenate DataFrames with the same columns using pd.concat
Instructions
Checkpoint 1 Enabled
1.
Cool T-Shirts Inc. just created a website for ordering their products. They want you to analyze two datasets for them:

visits contains information on all visits to their landing page
checkouts contains all users who began to checkout on their website
Use print to inspect each DataFrame.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
We want to know the amount of time from a user’s initial visit to the website to when they start to check out.

Use merge to combine visits and checkouts and save it to the variable v_to_c.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
In order to calculate the time between visiting and checking out, define a column of v_to_c called time that calculates the difference between checkout_time and visit_time for every row.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Use .mean() to calculate the average time to checkout and print that value to the terminal.
"""

import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print(visits)
print(checkouts)

v_to_c = pd.merge(visits, checkouts)

v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time

print(v_to_c)

print(v_to_c.time.mean())

