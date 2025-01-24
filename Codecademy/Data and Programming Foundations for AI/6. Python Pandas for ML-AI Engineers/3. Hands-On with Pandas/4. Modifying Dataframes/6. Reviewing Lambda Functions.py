"""
A lambda function is a way of defining a function in a single line of code. Usually, we would assign them to a variable.

For example, the following lambda function multiplies a number by 2 and then adds 3:

mylambda = lambda x: (x * 2) + 3
print(mylambda(5))


The output:

> 13


Lambda functions work with all types of variables, not just integers! Here is an example that takes in a string, assigns it to the temporary variable x, and then converts it into lowercase:

stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!"))


The output:

> "oh hi mark!"


Learn more about lambda functions in this article!

Instructions
Checkpoint 1 Enabled
1.
Create a lambda function mylambda that returns the first and last letters of a string, assuming the string is at least 2 characters long. For example,

print(mylambda('This is a string'))


should produce:

'Tg'

"""

mylambda = lambda x: x[0]+x[-1]
print(mylambda('Hello World'))