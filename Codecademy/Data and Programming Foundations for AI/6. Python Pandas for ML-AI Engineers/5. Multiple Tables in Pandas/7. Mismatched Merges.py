"""
In our previous examples, there were always matching values when we were performing our merges. What happens when that isn’t true?

Let’s imagine that our products table is out of date and is missing the newest product: Product 5. What happens when someone orders it?

Instructions
Checkpoint 1 Enabled
1.
We’ve just released a new product with product_id equal to 5. People are ordering this product, but we haven’t updated the products table.

In script.py, you’ll find two DataFrames: products and orders. Inspect these DataFrames using print.

Notice that the third order in orders is for the mysterious new product, but that there is no product_id 5 in products.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Merge orders and products and save it to the variable merged_df.

Inspect merged_df using:

print(merged_df)


What happened to order_id 3?
"""
import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print(orders)
print(products)

merged_df = pd.merge(
  orders,
  products
)
print(merged_df)