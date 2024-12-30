"""
Preview: Docs Lists are mutable sequence data types used for storing a comma-separated collection of objects in a single variable.
Lists
 can contain more than just numbers.

Let’s revisit our classroom example with heights:

Noelle is 61 inches tall
Ava is 70 inches tall
Sam is 67 inches tall
Mia is 64 inches tall
Instead of storing each student’s height, we can make a list that contains their names:

names = ["Noelle", "Ava", "Sam", "Mia"]

Copy to Clipboard

We can even combine multiple 
Preview: Docs Python is a strongly typed language. At runtime, it prevents typing errors and engages in little implicit type conversion.
data types
 in one list. For example, this list contains both a 
Preview: Docs Loading link description
string
 and an integer:

mixed_list_string_number = ["Noelle", 61]

Copy to Clipboard

Lists can contain any data type in Python! For example, this list contains a string, integer, boolean, and float.

mixed_list_common = ["Mia", 27, False, 0.5]

Copy to Clipboard

Let’s experiment with different data types in our own lists!

Instructions
Checkpoint 1 Enabled
1.
Add any additional string to the end of the list ints_and_strings.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Create a new list called sam_height_and_testscore that contains:

The string "Sam" (to represent Sam’s name)
The number 67 (to represent Sam’s height)
The float 85.5 (to represent Sam’s score)
The boolean True (to represent Sam passing the test)
Make sure to write the elements in exact order.
"""

ints_and_strings = [1, 2, 3, "four", "five", "hello"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]