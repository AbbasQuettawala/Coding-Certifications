"""
If we wanted to add multiple key : value pairs to a dictionary at once, we can use the 
Preview: Docs Loading link description
.update()
 method.

Looking at our sensors object from a previous exercise:

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

Copy to Clipboard

If we wanted to add 3 new rooms, we could use:

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

Copy to Clipboard

This would add all three items to the sensors dictionary.

Now, sensors looks like:

{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
In one line of code, add two new users to the user_ids dictionary:

theLooper, with an id of 138475
stringQueen, with an id of 85739
Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Print user_ids.
"""
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper":138475, "stringQueen":85739})
print(user_ids)