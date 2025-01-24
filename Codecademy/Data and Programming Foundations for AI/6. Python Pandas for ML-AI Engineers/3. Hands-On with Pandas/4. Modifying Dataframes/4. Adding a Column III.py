"""
Finally, you can add a new column by performing a function on the existing columns.

Maybe we want to add a column to our inventory table with the amount of sales tax that we need to charge for each item. The following code multiplies each Price by 0.075, the sales tax for our state:

df['Sales Tax'] = df.Price * 0.075


Now our table has a column called Sales Tax:

Product ID	Product Description	Cost to Manufacture	Price	Sales Tax
1	3 inch screw	0.50	0.75	0.06
2	2 inch nail	0.10	0.25	0.02
3	hammer	3.00	5.50	0.41
4	screwdriver	2.50	3.00	0.22
Instructions
Checkpoint 1 Enabled
1.
Add a column to df called 'Margin', which is equal to the difference between the Price and the Cost to Manufacture.
"""

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df['Margin'] = df['Price'] - df['Cost to Manufacture']

print(df)