"""
Good job! In this lesson, you learned

How to write a for loop.
How to use range in a loop.
How to write a while loop.
What infinite 
Preview: Docs Loading link description
loops
 are and how to avoid them.
How to control loops using break and continue.
How to write elegant loops as 
Preview: Docs Create lists concisely by applying an expression to each item in an iterable, with optional filtering based on a condition.
list comprehensions
.
Let’s get some more practice with these concepts!

Instructions
Checkpoint 1 Enabled
1.
Create a list called single_digits that consists of the numbers 0-9 (inclusive).

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Create a for loop that goes through single_digits and prints out each one.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Before the loop, create a list called squares. Assign it to be an empty list to begin with.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
After the for loop, print out squares.

Checkpoint 6 Step instruction is unavailable until previous steps are completed
6.
Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

Checkpoint 7 Step instruction is unavailable until previous steps are completed
7.
Print cubes.

Good job!
"""

# Your code below:
single_digits = range(10)
squares = []

for num in single_digits:
  print(num)
  squares.append(num **2)

print(squares)
cubes = [num ** 3 for num in single_digits]
print(cubes)