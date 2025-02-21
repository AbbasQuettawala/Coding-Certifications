"""
In the previous exercise, we learned how to use .rename() to merge two DataFrames whose columns don’t match.

If we don’t want to do that, we have another option. We could use the keywords left_on and right_on to specify which columns we want to perform the merge on. In the example below, the “left” table is the one that comes first (orders), and the “right” table is the one that comes second (customers). This syntax says that we should match the customer_id from orders to the id in customers.

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id')


If we use this syntax, we’ll end up with two columns called id, one from the first table and one from the second. Pandas won’t let you have two columns with the same name, so it will change them to id_x and id_y.

It will look like this:

id_x	customer_id	product_id	quantity	timestamp	id_y	customer_name	address	phone_number
1	2	3	1	2017-01-01 00:00:00	2	Jane Doe	456 Park Ave	949-867-5309
2	2	2	3	2017-01-01 00:00:00	2	Jane Doe	456 Park Ave	949-867-5309
3	3	1	1	2017-01-01 00:00:00	3	Joe Schmo	789 Broadway	112-358-1321
4	3	2	2	2016-02-01 00:00:00	3	Joe Schmo	789 Broadway	112-358-1321
5	3	3	3	2017-02-01 00:00:00	3	Joe Schmo	789 Broadway	112-358-1321
6	1	4	2	2017-03-01 00:00:00	1	John Smith	123 Main St.	212-123-4567
7	1	1	1	2017-02-02 00:00:00	1	John Smith	123 Main St.	212-123-4567
8	1	4	1	2017-02-02 00:00:00	1	John Smith	123 Main St.	212-123-4567
The new column names id_x and id_y aren’t very helpful for us when we read the table. We can help make them more useful by using the keyword suffixes. We can provide a list of suffixes to use instead of “_x” and “_y”.

For example, we could use the following code to make the suffixes reflect the table names:

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
    suffixes=['_order', '_customer']
)


The resulting table would look like this:

id_order	customer_id	product_id	quantity	timestamp	id_customer	customer_name	address	phone_number
1	2	3	1	2017-01-01 00:00:00	2	Jane Doe	456 Park Ave	949-867-5309
2	2	2	3	2017-01-01 00:00:00	2	Jane Doe	456 Park Ave	949-867-5309
3	3	1	1	2017-01-01 00:00:00	3	Joe Schmo	789 Broadway	112-358-1321
4	3	2	2	2016-02-01 00:00:00	3	Joe Schmo	789 Broadway	112-358-1321
5	3	3	3	2017-02-01 00:00:00	3	Joe Schmo	789 Broadway	112-358-1321
6	1	4	2	2017-03-01 00:00:00	1	John Smith	123 Main St.	212-123-4567
7	1	1	1	2017-02-02 00:00:00	1	John Smith	123 Main St.	212-123-4567
8	1	4	1	2017-02-02 00:00:00	1	John Smith	123 Main St.	212-123-4567
Instructions
Checkpoint 1 Enabled
1.
Merge orders and products using left_on and right_on. Use the suffixes _orders and _products. Save your results to the variable orders_products.

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
  products,
  left_on = 'customer_id',
  right_on = 'id',
  suffixes = ['_orders', '_products']
)

print(orders_products)