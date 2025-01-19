"""
Welcome! Let’s dive into lambda functions by exploring the in keyword!

This lesson will help you review lambda functions by providing some challenge exercises. If you need a refresher on the syntax of lambda functions, review this article on lambda functions.

In Python, you can check if a string contains a substring by using the keyword in. For example, the line:

return "I" in "Team"


would return False, as there is no "I" in "Team". However:

return "I" in "I love Python"


returns True, because there is an "I" in "I love Python".

Remember that to make a lambda function you can use the syntax:

lambda my_input: <my_input modified somehow>


For example, a lambda that would return my_input plus 1 would look like:

plus_one = lambda my_input: my_input+1


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named contains_a that takes an input word and returns True if the input contains the letter 'a'. Otherwise, return False.
"""

#Write your lambda function here
contains_a = lambda word: "a" in word

print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))