"""
By default, 
Preview: Docs Returns a sequence of numbers based on the given range
range()
 creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.

For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

my_list = range(2, 9)
print(list(my_list))

Copy to Clipboard

Would output:

[2, 3, 4, 5, 6, 7, 8]

Copy to Clipboard

If we use a third input, we can create a list that “skips” numbers.

For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:

my_range2 = range(2, 9, 2)
print(list(my_range2))

Copy to Clipboard

Would output:

[2, 4, 6, 8]

Copy to Clipboard

We can skip as many numbers as we want!

For example, we’ll start at 1 and skip in increments of 10 between each number until we get to 99 (one before 100):

my_range3 = range(1, 100, 10)
print(list(my_range3))

Copy to Clipboard

Would output:

[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

Copy to Clipboard

Our list stops at 91 because the next number in the sequence would be 101, which is greater than or equal to 100 (our stopping point).

Let’s experiment with our additional range() inputs!

Instructions
Checkpoint 1 Enabled
1.
Modify the range() function that created the range range_five_three such that it:

Starts at 5
Has a difference of 3 between each item
Ends before 15
Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Create a range called range_diff_five that:

Starts at 0
Has a difference of 5 between each item
Ends before 40
"""

# Your code below: 

range_five_three = range(5, 15, 3)
range_diff_five = range(0,40, 5)
