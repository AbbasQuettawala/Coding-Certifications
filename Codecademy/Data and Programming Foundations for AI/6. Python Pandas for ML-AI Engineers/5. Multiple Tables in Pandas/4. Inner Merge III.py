"""
In addition to using pd.merge(), each 
Preview: Docs Loading link description
DataFrame
 has its own .merge() method. For instance, if you wanted to merge orders with customers, you could use:

new_df = orders.merge(customers)


This produces the same DataFrame as if we had called pd.merge(orders, customers).

We generally use this when we are joining more than two DataFrames together because we can “chain” the commands. The following command would merge orders to customers, and then the resulting DataFrame to products:

big_df = orders.merge(customers)\
    .merge(products)


Instructions
Checkpoint 1 Enabled
1.
We have some more data from Cool T-Shirts Inc. The number of men’s and women’s t-shirts sold per month is in a file called men_women_sales.csv. Load this data into a DataFrame called men_women.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Merge all three DataFrames (sales, targets, and men_women) into one big DataFrame called all_data.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Display all_data using print.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Cool T-Shirts Inc. thinks that they have more revenue in months where they sell more women’s t-shirts.

Select the rows of all_data where:

revenue is greater than target
AND

women is greater than men
Save your answer to the variable results.
"""

import codecademylib3
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

men_women = pd.read_csv('men_women_sales.csv')
all_data = sales.merge(targets)\
    .merge(men_women)

print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]