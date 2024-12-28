"""
Programming languages offer a method of storing data for reuse. If there is a greeting we want to present, a date we need to reuse, or a user ID we need to remember we can create a 
Preview: Docs Loading link description
variable
 which can store a value. In Python, we 
Preview: Docs Loading link description
assign
 variables by using the equals sign (=).

message_string = "Hello there"
# Prints "Hello there"
print(message_string)

Copy to Clipboard

In the above example, we store the message “Hello there” in a variable called message_string. Variables can’t have spaces or symbols in their names other than an underscore (_). They can’t begin with numbers but they can have numbers after the first letter (e.g., cool_variable_5 is OK).

It’s no coincidence we call these creatures “variables”. If the context of a program changes, we can update a variable but perform the same logical process on it.

# Greeting
message_string = "Hello there"
print(message_string)

# Farewell
message_string = "Hasta la vista"
print(message_string)

Copy to Clipboard

Above, we create the variable message_string, assign a welcome message, and print the greeting. After we greet the user, we want to wish them goodbye. We then update message_string to a departure message and print that out.
"""
# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "Pizza"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner

# Printing out dinner
print("Dinner:")
print(meal)
