"""
You can use the modulo operator (%) with 10 to find the ones’ place of an integer.

Here are some examples:

>>> 41%10
1
>>> 2%10
2 
>>> 39%10
9
>>> 103%10
3
>>> 20%10
0


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named ones_place that returns the ones’ place of the input num.
"""

#Write your lambda function here
ones_place = lambda num: num%10

print(ones_place(123))
print(ones_place(4))
