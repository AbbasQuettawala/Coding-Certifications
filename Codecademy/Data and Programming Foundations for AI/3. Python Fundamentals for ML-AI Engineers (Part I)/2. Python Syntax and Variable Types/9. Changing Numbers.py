"""
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
Variables
 that are assigned numeric values can be treated the same as the numbers themselves. Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and literals (like the number 2 in this example). Performing arithmetic on variables does not change the variable — you can only update a variable using the = sign.

coffee_price = 1.50
number_of_coffees = 4

# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price 
coffee_price = 2.00

# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

Copy to Clipboard

We create two variables and assign numeric values to them. Then we perform a calculation on them. This doesn’t update the variables! When we update the coffee_price variable and perform the calculations again, they use the updated values for the variable!

"""


quilt_width = 8
quilt_length = 12

print(quilt_width * quilt_length)

quilt_length = 8

print(quilt_width * quilt_length)