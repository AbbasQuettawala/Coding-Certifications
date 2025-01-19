"""
Python makes math easy. To multiply, you can use *:

>>> 4*2
8
>>> 2*3
6
>>> 0*10
0
>>> 20*10
200


As a reminder, to return different output depending on different input, we can use if and else inside our lambda function:

add_or_subtract = lambda input_number: input_number - 1 if input_number >= 0 else input_number + 1


The function add_or_subtract will return your input minus 1 if your input is positive or 0, and otherwise will return your input plus 1.

Here are some examples of how it would work:

>>> add_or_subtract(0)
-1
>>> add_or_subtract(8)
7
>>> add_or_subtract(-4)
-3


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named double_or_zero that takes an integer named num. If num is greater than 10, return double num. Otherwise, return 0.
"""

#Write your lambda function here
double_or_zero = lambda num: num * 2 if num > 10 else num * 0
print(double_or_zero(15))
print(double_or_zero(5))