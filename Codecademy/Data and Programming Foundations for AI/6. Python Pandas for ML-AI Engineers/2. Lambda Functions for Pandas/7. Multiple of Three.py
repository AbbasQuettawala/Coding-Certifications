"""
In general, using %n will tell you if an integer is a multiple of n. If the result is 0, the integer is a multiple of n (since there is no remainder in the division):

>>> 4%4 #4 is a multiple of 4
0
>>> 12%5 #12 is not a multiple of 5
2 
>>> 9%2 #9 is not a multiple of 2
1
>>> 100%10 #100 is a multiple of 10
0


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named multiple_of_three that takes an integer named num. If num is a multiple of three, return "multiple of three". Otherwise, return "not a multiple".
"""

#Write your lambda function here
multiple_of_three = lambda num: "multiple of three" if num%3 == 0 else "not a multiple"
print(multiple_of_three(9))
print(multiple_of_three(10))
