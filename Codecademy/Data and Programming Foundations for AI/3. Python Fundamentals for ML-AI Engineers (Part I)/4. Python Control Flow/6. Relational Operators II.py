"""
Now that we’ve added conditional statements to our toolkit for building control flow, let’s explore more ways to create boolean expressions. So far we know two relational 
Preview: Docs Loading link description
operators
, equals and not equals, but there are a ton (well, four) more:

> greater than
>= greater than or equal to
< less than
<= less than or equal to
Let’s say we’re running a movie streaming platform and we want to write a program that checks if our users are over 13 when showing them a PG-13 movie. We could write something like:

if age <= 13:
  print("Sorry, parental control required")

Copy to Clipboard

This function will take the user’s age and compare it to the number 13. If age is less than or equal to 13, it will print out a message.

Let’s try some more!

Instructions
Checkpoint 1 Enabled
1.
Create an if statement that checks if x and y are equal, print the string below if so:

"These numbers are the same"

Copy to Clipboard

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate.

Write an if statement that checks if the student has enough credits to graduate. If they do, print the string:

"You have enough credits to graduate!"

Copy to Clipboard

Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?
"""
x = 20
y = 20

# Write the first if statement here:
if x == y:
  print("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits >= 120:
    print("You have enough credits to graduate!")

