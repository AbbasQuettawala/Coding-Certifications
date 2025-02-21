"""

Suppose we have the following three tables that describe our eCommerce business:

orders — a table with information on each transaction:
order_id	customer_id	product_id	quantity	timestamp
1	2	3	1	2017-01-01
2	2	2	3	2017-01-01
3	3	1	1	2017-01-01
4	3	2	2	2017-02-01
5	3	3	3	2017-02-01
6	1	4	2	2017-03-01
7	1	1	1	2017-02-02
8	1	4	1	2017-02-02

products — a table with product IDs, descriptions, and prices:
product_id	description	price
1	thing-a-ma-jig	5
2	whatcha-ma-call-it	10
3	doo-hickey	7
4	gizmo	3

customers — a table with customer names and contact information:
customer_id	customer_name	address	phone_number
1	John Smith	123 Main St.	212-123-4567
2	Jane Doe	456 Park Ave.	949-867-5309
3	Joe Schmo	798 Broadway	112-358-1321

If we just look at the orders table, we can’t really tell what’s happened in each order. However, if we refer to the other tables, we can get a more complete picture.

Let’s examine the order with an order_id of 1. It was purchased by Customer 2. To find out the customer’s name, we look at the customers table and look for the item with a customer_id value of 2. We can see that Customer 2’s name is Jane Doe and that she lives at 456 Park Ave.

Doing this kind of matching is called merging two DataFrames.

Instructions
Checkpoint 1 Enabled
1.
Examine the orders and products tables.

What is the description of the product that was ordered in Order 3?

Give your answer as a string assigned to the variable order_3_description.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Examine the orders and customers tables.

What is the phone_number of the customer in Order 5?

Give your answer as a string assigned to the variable order_5_phone_number.
"""

import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)
print(products)
print(customers)

order_3_description = 'thing-a-ma-jig'
order_5_phone_number = '112-358-1321'
