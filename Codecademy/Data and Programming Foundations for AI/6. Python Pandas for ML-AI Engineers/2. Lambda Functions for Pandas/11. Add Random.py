"""
random.randint(a,b) will return an integer between a and b (inclusive).

So, random.randint(5, 8) could return any integer between 5 and 8 including both 5 and 8.

random.randint(0, 100) could return any integer between 0 and 100 including both 0 and 100.

Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named add_random that takes an input named num. The function should return num plus a random integer number between 1 and 10 (inclusive).
"""
import random
#Write your lambda function here
add_random = lambda num: num + random.randint(1, 10)

print(add_random(5))
print(add_random(100))