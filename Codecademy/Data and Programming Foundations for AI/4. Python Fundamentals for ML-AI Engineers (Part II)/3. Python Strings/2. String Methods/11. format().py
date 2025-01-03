"""
Python also provides a handy string method for including 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
 in 
Preview: Docs Loading link description
strings
. This method is .format(). .format() takes variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for where those variables will be imported.

Consider the following function:

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

Copy to Clipboard

The function favorite_song_statement takes two arguments, song and artist, then returns a string that includes both of the arguments and prints a sentence. Note: .format() can take as many arguments as there are {} in the string it is run on, which in this case is two.

Here’s an example of the function being run:

print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."

Copy to Clipboard

Now you may be asking yourself, I could have written this function using string concatenation instead of .format(), why is this method better? The answer is legibility and reusability. It is much easier to picture the end result .format() than it is to picture the end result of string concatenation and legibility is everything. You can also reuse the same base string with different variables, allowing you to cut down on unnecessary, hard to interpret code.

Instructions
Checkpoint 1 Enabled
1.
Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The function should use .format() to return the following string:

 The poem "[TITLE]" is written by [POET].

Copy to Clipboard

For example, if the function is given the inputs

poem_title_card("I Hear America Singing", "Walt Whitman")

Copy to Clipboard

It should return the string

The poem "I Hear America Singing" is written by Walt Whitman.

"""
def poem_title_card(title, poet):
  return "The poem {} is written by {}.".format(title,poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman"))