"""
10 min
In this lesson, you’ve learned how to go through 
Preview: Docs A dictionary is a data set of key-value pairs.
dictionaries
 and access keys and values in different ways. Specifically, you have seen how to:

Use a key to get a value from a dictionary
Check for existence of keys
Remove a key: value pair from a dictionary
Iterate through keys and values in dictionaries
Instructions
Checkpoint 1 Enabled
1.
We have provided a pack of tarot cards, tarot. You are going to do a three card spread of your past, present, and future.

Create an empty dictionary called spread.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
The first card you draw is card 13. Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
The second card you draw is card 22. Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
The third card you draw is card 10. Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
Iterate through the items in the spread dictionary and for each key: value pair, print out a string that says:

Your {key} is the {value} card.

Copy to Clipboard

Checkpoint 6 Step instruction is unavailable until previous steps are completed
6.
Congratulations! You have learned about how to modify and use dictionaries.
Hit the Run button one more time when you are ready to continue.
"""
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)
for key,value in spread.items():
  print("Your " + key + " is the " + value + " card.")


