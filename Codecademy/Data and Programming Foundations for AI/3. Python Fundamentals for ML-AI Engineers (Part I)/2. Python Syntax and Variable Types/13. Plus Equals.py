"""
Python offers a shorthand for updating 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
. When you have a number saved in a variable and want to add to the current value of the variable, you can use the += 
Preview: Docs Operators are used to perform various operations on variables and values.
(plus-equals) operator
.

# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

Copy to Clipboard

Above, we keep a running count of the number of miles a person has gone hiking over time. Instead of recalculating from the start, we keep a grand total and update it when we’ve gone hiking further.

The plus-equals operator also can be used for string concatenation, like so:

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

Copy to Clipboard

We create the social media caption for the photograph of nature we took on our hike, but then update the caption to include important social media tags we almost forgot.
"""

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += fun_books
total_price += nice_sweater

print("The total price is", total_price)