"""
The most recent hire at Copeland’s Corporate Company is a fellow named Rob Daily. Unfortunately, Human Resources seem to have made a bit of a typo and sent over the wrong first_name.

Try changing the first character of first_name by running

first_name[0] = "R"

Copy to Clipboard

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Oh right! Strings are immutable, so we can’t change an individual character. Okay that’s no problem—we can still fix this!

Delete the code you just wrote for step 1.

Then, concatenate the string "R" with a slice of first_name that includes everything but the first character, "B", and save it to a new string fixed_first_name.

"""
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]
