"""
We can add a single element to a list using the 
Preview: Docs Adds an item to end of the list.
.append()
 Python method.

Suppose we have an empty list called garden:

garden = []

Copy to Clipboard

We can add the element "Tomatoes" by using the .append() method:

garden.append("Tomatoes")

print(garden)

Copy to Clipboard

Will output:

['Tomatoes']

Copy to Clipboard

We see that garden now contains "Tomatoes"!

When we use .append() on a list that already has elements, our new element is added to the end of the list:

# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]

# Append a new element
garden.append("Green Beans")
print(garden)

Copy to Clipboard

Will output:

['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']

Copy to Clipboard

Let’s use the .append() method to manipulate a list.

Instructions
Checkpoint 1 Enabled
1.
Jiho works for a gardening store called Petal Power. Jiho keeps a record of orders in a list called orders.

Use print to inspect the orders he has received today.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Jiho just received a new order for "tulips". Use append to add this string to orders.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Another order has come in! Use append to add "roses" to orders.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Use print to inspect the orders Jiho has received today.
"""

orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)