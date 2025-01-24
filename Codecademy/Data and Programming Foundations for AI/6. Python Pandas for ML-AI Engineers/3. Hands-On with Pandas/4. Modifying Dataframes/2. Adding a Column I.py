"""
Sometimes, we want to add a column to an existing DataFrame. We might want to add new information or perform a calculation based on the data that we already have.

One way that we can add a new column is by giving a list of the same length as the existing DataFrame.

Suppose we own a hardware store called The Handy Woman and have a DataFrame containing inventory information:

Product ID	Product Description	Cost to Manufacture	Price
1	3 inch screw	0.50	0.75
2	2 inch nail	0.10	0.25
3	hammer	3.00	5.50
4	screwdriver	2.50	3.00

It looks like the actual quantity of each product in our warehouse is missing!

Let’s use the following code to add that information to our DataFrame.

df['Quantity'] = [100, 150, 50, 35]


Our new DataFrame looks like this:

Product ID	Product Description	Cost to Manufacture	Price	Quantity
1	3 inch screw	0.50	0.75	100
2	2 inch nail	0.10	0.25	150
3	hammer	3.00	5.50	50
4	screwdriver	2.50	3.00	35
Instructions
Checkpoint 1 Enabled
1.
The DataFrame df contains information on products sold at a hardware store. Add a column to df called 'Sold in Bulk?', which indicates if the product is sold in bulk or individually. The final table should look like this:

Product ID	Product Description	Cost to Manufacture	Price	Sold in Bulk?
1	3 inch screw	0.50	0.75	Yes
2	2 inch nail	0.10	0.25	Yes
3	hammer	3.00	5.50	No
4	screwdriver	2.50	3.00	No
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

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

print(df)