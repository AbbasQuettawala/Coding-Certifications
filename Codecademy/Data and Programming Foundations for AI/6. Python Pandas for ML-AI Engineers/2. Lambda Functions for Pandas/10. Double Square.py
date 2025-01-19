"""
You can find the square of a number by multiplying it by itself:

eight_squared = 8*8
#The value of eight_squared is now 64


or by using the exponential operator **:

seven_squared = 7**2
#The value of seven_squared is now 49


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named double_square that takes an input named num. The function should return twice the square of num.
"""

#Write your lambda function here
double_square = lambda num: 2 * num * num

print(double_square(5))
print(double_square(3))