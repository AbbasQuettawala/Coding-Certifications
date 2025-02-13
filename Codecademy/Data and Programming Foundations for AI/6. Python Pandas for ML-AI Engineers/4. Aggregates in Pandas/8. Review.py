"""
This lesson introduced you to aggregates in Pandas. You learned:

How to perform aggregate statistics over individual rows with the same value using 
Preview: Docs The GroupBy object is returned by calls to `.groupby()` on a Series or DataFrame.
groupby
.
How to rearrange a 
Preview: Docs Loading link description
DataFrame
 into a pivot table, a great way to compare data across two dimensions.
Instructions
Checkpoint 1 Enabled
1.
Let’s examine some more data from ShoeFly.com. This time, we’ll be looking at data about user visits to the website (the same dataset that you saw in the introduction to this lesson).

The data is a DataFrame called user_visits. Use print and head() to examine the first few rows of the DataFrame.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
The column utm_source contains information about how users got to ShoeFly’s homepage. For instance, if utm_source = Facebook, then the user came to ShoeFly by clicking on an ad on Facebook.com.

Use a groupby statement to calculate how many visits came from each of the different sources. Save your answer to the variable click_source.

Remember to use reset_index()!

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Paste the following code into script.py so that you can see the results of your previous groupby:

print(click_source)


Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Our Marketing department thinks that the traffic to our site has been changing over the past few months. Use groupby to calculate the number of visits to our site from each utm_source for each month. Save your answer to the variable click_source_by_month.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
The head of Marketing is complaining that this table is hard to read. Use pivot to create a pivot table where the rows are utm_source and the columns are month. Save your results to the variable click_source_by_month_pivot.

It should look something like this:

utm_source	1 - January	2 - February	3 - March
email	…	…	…
facebook	…	…	…
google	…	…	…
twitter	…	…	…
yahoo	…	…	…
Checkpoint 6 Step instruction is unavailable until previous steps are completed
6.
View your pivot table by pasting the following code into script.py:


"""

import codecademylib3
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())
click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(columns = 'month', index = 'utm_source', values = 'id').reset_index()
print(click_source_by_month_pivot)

