"""
If we provide an argument for 
Preview: Docs Loading link description
.split()
 we can dictate the character we want our string to be split on. This argument should be provided as a string itself.

Consider the following example:

greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
# => ['sa', 'ta', 'a']

Copy to Clipboard

We provided 'n' as the argument for .split() so our string “santana” got split at each 'n' character into a list of three strings.

What do you think happens if we split the same string at 'a'?

print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', '']

Copy to Clipboard

Notice that there is an unexpected extra '' string in this list. When you split a string on a character that it also ends with, you’ll end up with an empty string at the end of the list.

You can use any string as the argument for .split(), making it a versatile and powerful tool.

Instructions
Checkpoint 1 Enabled
1.
Your boss at the Poetry organization sent over a bunch of author names that he wants you to prepare for importing into the database. Annoyingly, he sent them over as a long string with the names separated by commas.

Using .split() and the provided string, create a list called author_names containing each individual author name as it’s own string.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Great work, but now it turns out they didn’t want poet’s first names (why didn’t they just say that the first time!?)

Create another list called author_last_names that only contains the last names of the poets in the provided string.
"""
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)
