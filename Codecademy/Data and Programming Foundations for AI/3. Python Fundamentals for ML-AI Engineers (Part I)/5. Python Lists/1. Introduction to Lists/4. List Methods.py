"""
As we start exploring lists further in the next exercises, we will encounter the concept of a method.

In Python, for any specific data-type ( 
Preview: Docs Loading link description
strings
, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data. We call this built-in functionality a method.

For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( ).

An example of a popular list method is 
Preview: Docs Loading link description
.append()
, which allows us to add an element to the end of a list.

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)

Copy to Clipboard

Will output:

['This', 'is', 'an', 'example', 'list']

Copy to Clipboard

Instructions
We will be exploring .append() and many other methods in the upcoming exercises but for now take a second to examine and play around with the code for two common list methods.
"""

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)