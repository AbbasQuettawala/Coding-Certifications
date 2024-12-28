"""
Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. Python offers a solution: 
Preview: Docs A string is a sequence of characters contained within a pair of single quotes or double quotes.
multi-line strings
. By using three quote-marks ( or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.

leaves_of_grass = """
"""
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
"""

Copy to Clipboard

In the above example, we assign a famous poet’s words to a variable. Even though the quote contains multiple linebreaks, the code works!

If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.

"""
# Assign the string here
to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?


"""


print(to_you)