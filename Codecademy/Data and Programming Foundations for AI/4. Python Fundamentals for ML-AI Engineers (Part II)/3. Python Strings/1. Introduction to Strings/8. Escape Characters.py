"""
Occasionally when working with 
Preview: Docs Loading link description
strings
, you’ll find that you want to include characters that already have a special meaning in python. For example let’s say I create the string

 favorite_fruit_conversation = "He said, "blueberries are my favorite!""

Copy to Clipboard

We’ll have accidentally ended the string before we wanted to by including the " character. The way we can do this is by introducing escape characters. By adding a backslash in front of the special character we want to escape, \", we can include it in a string.

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

Copy to Clipboard

Now it works!

Instructions
Checkpoint 1 Enabled
1.
When Rob Daily (remember him? From the last exercise?) set up his account he set his password to be

theycallme"crazy"91

Copy to Clipboard

His password was causing some errors in the system because of the " marks. Rewrite his password using escape characters and save it to the variable password.
"""
password = "theycallme\"crazy\"91"