"""
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

We can sort a list using the method 
Preview: Docs Sorts the contents of the list it is called on.
.sort()
.

Suppose that we have a list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

Copy to Clipboard

Let’s see what happens when we apply .sort():

names.sort()
print(names)

Copy to Clipboard

Would output:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

Copy to Clipboard

As we can see, the .sort() method sorted our list of names in alphabetical order.

.sort() also provides us the option to go in reverse. Instead of sorting in ascending order like we just saw, we can do so in descending order.

names.sort(reverse=True)
print(names)

Copy to Clipboard

Would output:

['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

Copy to Clipboard

Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. If we do assign the result of the method, it would assign the value of None to the variable.

Let’s experiment sorting various lists!

Instructions
Checkpoint 1 Enabled
1.
Use .sort() to sort addresses.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Use print() to see how addresses changed.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Use print to examine sorted_cities. Why is it not the sorted version of cities?

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
Edit the .sort() call on cities such that it sorts the cities in reverse order (descending).

Print cities to see the result.
"""

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse = True)

addresses.sort()
print(addresses)
print(sorted_cities)