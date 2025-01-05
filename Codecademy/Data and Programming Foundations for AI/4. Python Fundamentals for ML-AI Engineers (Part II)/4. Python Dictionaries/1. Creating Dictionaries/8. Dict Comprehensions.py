"""
Let’s say we have two 
Preview: Docs Loading link description
lists
 that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

Copy to Clipboard

Python allows you to create a dictionary using a dict comprehension, with this syntax:

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

Copy to Clipboard

Remember that 
Preview: Docs Loading link description
zip()
 combines two lists into an iterator of 
Preview: Docs Loading link description
tuples
 with the list elements paired together. This dict comprehension:

Takes a pair from the iterator of tuples
Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
Creates a key : value item in the students dictionary
Repeats steps 1-3 for the entire iterator of pairs
Instructions
Checkpoint 1 Enabled
1.
You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through the zipped_drinks iterator and turns each tuple pair into a key:value item.
"""
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
