"""
In Python, %, or the modulo operator, returns the remainder after division.

>>> 4%2 #This divides evenly
0
>>> 7%3 #7/3 has a remainder of 1
1
>>> 27%10
7
>>> 30%10
0


You can use % 2 to determine if a number is even or odd. If it is even, there should be no remainder (an output of 0). If it is odd, there should be a remainder of 1:

>>> 4%2 
0
>>> 7%2
1
>>> 9%2
1
>>> 0%2
0


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named even_or_odd that takes an integer named num. If num is even, return "even". If num is odd, return "odd".
"""

#Write your lambda function here
even_or_odd = lambda num: "even" if num%2 == 0 else "odd"

print(even_or_odd(10))
print(even_or_odd(5))
