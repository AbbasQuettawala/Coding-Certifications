"""
In the previous example, the .merge() function “knew” how to combine tables based on the columns that were the same between two tables. For instance, products and orders both had a column called product_id. This won’t always be true when we want to perform a merge.

Generally, the products and customers DataFrames would not have the columns product_id or customer_id. Instead, they would both be called id and it would be implied that the id was the product_id for the products table and customer_id for the customers table. They would look like this:

Customers
id	customer_name	address	phone_number
1	John Smith	123 Main St.	212-123-4567
2	Jane Doe	456 Park Ave.	949-867-5309
3	Joe Schmo	798 Broadway	112-358-1321
Products
id	description	price
1	thing-a-ma-jig	5
2	whatcha-ma-call-it	10
3	doo-hickey	7
4	gizmo	3

**How would this affect our merges?**
Because the id columns would mean something different in each table, our default merges would be wrong.

One way that we could address this problem is to use .rename() to rename the columns for our merges. In the example below, we will rename the column id to customer_id, so that orders and customers have a common column for the merge.

pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))


Instructions
Checkpoint 1 Enabled
1.
Merge orders and products using .rename(). Save your results to the variable orders_products.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Display orders_products using print.
"""

import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(
  orders,
  products.rename(columns = {'id': 'product_id'})
)
print(orders_products)