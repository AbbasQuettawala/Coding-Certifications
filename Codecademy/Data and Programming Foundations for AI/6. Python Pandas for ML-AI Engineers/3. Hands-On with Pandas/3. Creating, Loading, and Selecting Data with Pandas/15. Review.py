"""
You’ve completed the lesson! You’ve just learned the basics of working with a single table in Pandas, including:

Create a table from scratch
Loading data from another file
Selecting certain rows or columns of a table
Let’s practice what you’ve learned.

Instructions
Checkpoint 1 Passed
1.
In this example, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store. You’ve seen this data; now it’s your turn to work with it!

Load the data from shoefly.csv into the variable orders.

Checkpoint 2 Passed
2.
Inspect the first 5 lines of the data.

Checkpoint 3 Passed
3.
Your marketing department wants to send out an email blast to everyone who ordered shoes!

Select all of the email addresses from the column email and save them to a variable called emails.

Checkpoint 4 Passed
4.
Frances Palmer claims that her order was wrong. What did Frances Palmer order?

Use logic to select that row of orders and save it to the variable frances_palmer.

Checkpoint 5 Passed
5.
We need some customer reviews for our comfortable shoes. Select all orders for shoe_type: clogs, boots, and ballet flats and save them to the variable comfy_shoes.

Remember to use isin to select multiple values from a list! If we wanted to select shoes that were blue, green, or red, we’d use:


"""


import codecademylib3
import pandas as pd
orders = pd.read_csv("shoefly.csv")
print(orders.head(4))
emails = orders['email']
frances_palmer = orders[(orders.first_name == 'Frances')]
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
