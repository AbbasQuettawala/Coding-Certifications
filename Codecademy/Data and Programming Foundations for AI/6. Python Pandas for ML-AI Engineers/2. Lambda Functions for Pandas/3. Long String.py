"""
To find the number of characters in a string, we use len. This block of code:

print(len("Hello"))
print(len("world!"))
print(len("Hello, world!"))


would print out:

5
6
13


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named long_string that takes an input str and returns True if the string has over 12 characters in it. Otherwise, return False.
"""

#Write your lambda function here
long_string = lambda string: len(string) > 12

print(long_string("short"))
print(long_string("photosynthesis"))
