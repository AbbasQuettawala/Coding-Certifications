"""
In Python, it is common to want to count occurrences of an item in a list.

Suppose we have a list called letters that represents the letters in the word “Mississippi”:

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]

Copy to Clipboard

If we want to know how many times i appears in this word, we can use the list method called 
Preview: Docs Loading link description
.count()
:

num_i = letters.count("i")
print(num_i)

Copy to Clipboard

Would output:

4

Copy to Clipboard

Notice that since .count() returns a value, we can assign it to a variable to use it.

We can even use .count() to count element appearances in a two-dimensional list.

Let’s use the list number_collection as an example:

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

Copy to Clipboard

If we wanted to know how often the sublist [100, 200] appears:

num_pairs = number_collection.count([100, 200])
print(num_pairs)

Copy to Clipboard

Would output:

2

Copy to Clipboard

Let’s count some list items using the .count() method!

Instructions
Checkpoint 1 Enabled
1.
Mrs. Wilson’s class is voting for class president. She has saved each student’s vote into the list votes.

Use .count() to determine how many students voted for "Jake" and save the value to a variable called jake_votes.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Use print() to examine jake_votes.
"""

otes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)