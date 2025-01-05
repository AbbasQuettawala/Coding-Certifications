"""
To add a single key: value pair to a dictionary, we can use the syntax:

dictionary[key] = value
For example, if we had our menu dictionary from the first exercise:

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

Copy to Clipboard

And we wanted to add a new item, "cheesecake" for 8 dollars, we could use:

menu["cheesecake"] = 8

Copy to Clipboard

Now, menu looks like:

{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
Create an empty dictionary called animals_in_zoo.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Walking around the zoo, you see 8 zebras. Add "zebras" to animals_in_zoo as a key with a value of 8.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
The primate house was bananas! Add "monkeys" to animals_in_zoo as a key with a value of 12.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
As you leave the zoo, you are saddened that you did not see any dinosaurs. Add "dinosaurs" to animals_in_zoo as a key with a value of 0.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
Print animals_in_zoo.
"""
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)