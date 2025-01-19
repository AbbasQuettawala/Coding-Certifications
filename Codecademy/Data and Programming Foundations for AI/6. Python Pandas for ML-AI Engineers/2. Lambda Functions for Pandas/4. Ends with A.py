"""
You can get a character of a string string_name by using the syntax string_name[index], where index is the place of character you want to get, starting at 0. The last character in the string is string_name[-1].

For example:

my_string = "Whoa! A seesaw"
print(my_string[0])
print(my_string[2])
print(my_string[-1])


would print

"W"
"o"
"w"


Instructions
Checkpoint 1 Enabled
1.
Create a lambda function named ends_in_a that takes an input str and returns True if the last character in the string is an a. Otherwise, return False.
"""

#Write your lambda function here
ends_in_a = lambda string: 'a' in string[-1]

print(ends_in_a("data"))
print(ends_in_a("aardvark"))
