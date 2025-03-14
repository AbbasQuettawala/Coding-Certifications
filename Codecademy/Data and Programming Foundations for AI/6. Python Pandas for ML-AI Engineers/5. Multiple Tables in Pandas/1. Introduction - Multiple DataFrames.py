"""
In order to efficiently store data, we often spread related information across multiple tables.

For instance, imagine that we own an e-commerce business and we want to track the products that have been ordered from our website.

We could have one table with all of the following information:

order_id
customer_id
customer_name
customer_address
customer_phone_number
product_id
product_description
product_price
quantity
timestamp
However, a lot of this information would be repeated. If the same customer makes multiple orders, that customer’s name, address, and phone number will be reported multiple times. If the same product is ordered by multiple customers, then the product price and description will be repeated. This will make our orders table big and unmanageable.

So instead, we can split our data into three tables:

orders would contain the information necessary to describe an order: order_id, customer_id, product_id, quantity, and timestamp
products would contain the information to describe each product: product_id, product_description and product_price
customers would contain the information for each customer: customer_id, customer_name, customer_address, and customer_phone_number
In this lesson, we will learn the Pandas commands that help us work with data stored in multiple tables.

Instructions
Checkpoint 1 Enabled
1.
In script.py, we’ve loaded in three DataFrames: orders, products, and customers.

Start by inspecting orders using the following code:

print(orders)


Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Now inspect products using the following code:

print(products)


Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Now inspect customers using the following code:

print(customers)

"""

import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)
print(products)
print(customers)