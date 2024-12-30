"""
What if we want to select the last element of a list?

We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

Consider the following list with 6 elements:

pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]

Copy to Clipboard

If we select the -1 index, we get the final element, "love".

print(pancake_recipe[-1])

Copy to Clipboard

Would output:

love

Copy to Clipboard

This is equivalent to selecting the element with index 5:

print(pancake_recipe[5])

Copy to Clipboard

Would output:

love

Copy to Clipboard

Here are the negative index numbers for our list:

Element	Index
"eggs"	-6
"flour"	-5
"butter"	-4
"milk"	-3
"sugar"	-2
"love"	-1
Instructions
Checkpoint 1 Enabled
1.
Create a variable called last_element.

Assign the last element in shopping_list to the variable last_element using a negative index.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Now select the element with index 5 and save it to the variable index5_element.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Use print to display both index5_element and last_element.

Note that they are equal to "cereal"!

"""

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(index5_element)
print(last_element)