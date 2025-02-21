"""
It is easy to do this kind of matching for one row, but hard to do it for multiple rows.

Luckily, Pandas can efficiently do this for the entire table. We use the .merge() method.

The .merge() method looks for columns that are common between two DataFrames and then looks for rows where those column’s values are the same. It then combines the matching rows into a single row in a new table.

We can call the pd.merge() method with two tables like this:

new_df = pd.merge(orders, customers)


This will match up all of the customer information to the orders that each customer made.

Instructions
Checkpoint 1 Enabled
1.
You are an analyst at Cool T-Shirts Inc. You are going to help them analyze some of their sales data.

There are two DataFrames defined in the file script.py:

sales contains the monthly revenue for Cool T-Shirts Inc. It has two columns: month and revenue.
targets contains the goals for monthly revenue for each month. It has two columns: month and target.
Create a new DataFrame sales_vs_targets which contains the merge of sales and targets.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Display sales_vs_targets using print.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Cool T-Shirts Inc. wants to know the months when they crushed their targets.

Select the rows from sales_vs_targets where revenue is greater than target. Save these rows to the variable crushing_it.
"""

import codecademylib3
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]