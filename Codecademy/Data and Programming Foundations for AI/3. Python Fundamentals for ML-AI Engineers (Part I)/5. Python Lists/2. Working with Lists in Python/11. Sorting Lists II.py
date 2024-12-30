"""
A second way of sorting a list in Python is to use the built-in function sorted().

The 
Preview: Docs Takes in an iterator object, such as a list, tuple, dictionary, set, or string, and sorts it according to a parameter.
sorted()
 function is different from the 
Preview: Docs Sorts the contents of the list it is called on.
.sort()
 method in two ways:

It comes before a list, instead of after as all built-in 
Preview: Docs Functions allow tasks to be performed multiple times within a program without having to be rewritten.
functions
 do.
It generates a new list rather than modifying the one that already exists.
Let’s return to our list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

Copy to Clipboard

Using sorted(), we can create a new list, called sorted_names:

sorted_names = sorted(names)
print(sorted_names)

Copy to Clipboard

This yields the list sorted alphabetically:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

Copy to Clipboard

Note that using sorted did not change names:

print(names)

Copy to Clipboard

Would output:

['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
Use sorted() to order games and create a new list called games_sorted.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Print both games and games_sorted. How are they different?
"""
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)
