"""
Let’s return to our garden.

garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]

Copy to Clipboard

Unfortunately, we forgot to water our cauliflower and we don’t think it is going to recover.

Thankfully our friend Jiho from Petal Power came to the rescue. Jiho gifted us some strawberry seeds. We will replace the cauliflower with our new seeds.

We will need to modify the list to accommodate the change to our garden list. To change a value in a list, reassign the value using the specific index.

garden[2] = "Strawberries"

print(garden)

Copy to Clipboard

Will output:

["Tomatoes", "Green Beans", "Strawberries", "Grapes"]

Copy to Clipboard

Negative indices will work as well.

garden[-1] = "Raspberries"

print(garden)

Copy to Clipboard

Will output:

["Tomatoes", "Green Beans", "Strawberries", "Raspberries"]

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
We have decided to start selling some of our garden produce. Word around our town has spread and people are interested in getting some of our delicious vegetables and fruit.

We decided to create a waitlist to make sure we can sell to all of our new customers!

Define a list called garden_waitlist and set the value to contain our customers (in order): "Jiho", "Adam", "Sonny", and "Alisha".

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
"Adam" decided his fridge is too full at the moment and asked us to remove him from the waitlist and make space for one of our other townsfolk.

Replace "Adam" with our other interested customer "Calla" using the index method we used in the narrative.

Print garden_waitlist to see the change!

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Alisha realized she was already stocked with all the items we are selling. She asked us to replace her with her friend Alex who just ran out.

Replace Alisha with Alex using a negative index.

Print garden_waitlist again to see the change!
"""

# Your code below:
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)