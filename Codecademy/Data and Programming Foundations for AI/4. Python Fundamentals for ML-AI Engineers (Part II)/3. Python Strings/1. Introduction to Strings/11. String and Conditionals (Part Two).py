"""
There’s an even easier way than iterating through the entire string to determine if a character is in a string. We can do this type of check more efficiently using in. in checks if one string is part of another string.

Here is what the syntax of in looks like:

letter in word

Copy to Clipboard

Here, letter in word is a boolean expression that is True if the string letter is in the string word. Here are some examples:

print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

Copy to Clipboard

In fact, this method is more powerful than the function you wrote in the last exercise because it not only works with letters, but with entire 
Preview: Docs Loading link description
strings
 as well.

print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False

Copy to Clipboard

It can be helpful to include more than one boolean expression in the same line of code. To do this, use and or and not in between the boolean expressions.

print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True

Copy to Clipboard

The first example above is False because ONE of the expressions was False; there is no “e” in “carrot”. The second example is True because there is an “e” in “blueberry” and not an “e” in “carrot”; both expressions are True.

Instructions
Checkpoint 1 Enabled
1.
Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string.

For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

The letters in the returned list should be unique. For example,

common_letters("banana", "cream")

Copy to Clipboard

should return ['a']
"""

def contains(big_string, little_string):
  if little_string in big_string:
    return True
  return False


def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common