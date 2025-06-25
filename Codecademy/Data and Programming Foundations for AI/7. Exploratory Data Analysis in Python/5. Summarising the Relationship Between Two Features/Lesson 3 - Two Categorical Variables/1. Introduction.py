'''
In this lesson, we will cover ways of examining an association between two categorical 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
.

As an example, we’ll explore a sample of data from the Narcissistic Personality Inventory (NPI-40), a personality test with 40 questions about personal preferences and self-view. There are two possible responses to each question. The sample we’ll be working with contains responses to the following:

influence: yes = I have a natural talent for influencing people; no = I am not good at influencing people.
blend_in: yes = I prefer to blend in with the crowd; no = I like to be the center of attention.
special: yes = I think I am a special person; no = I am no better or worse than most people.
leader: yes = I see myself as a good leader; no = I am not sure if I would make a good leader.
authority: yes = I like to have authority over other people; no = I don’t mind following orders.
As you might guess, responses to some of these questions are associated. For example, if we know whether someone views themself as a good leader, we may also find that they’re more likely to like having authority. In this lesson we’ll learn how to assess whether an association exists between any two of these variables.

Instructions
Checkpoint 1 Passed
1.
Data from the Narcissistic Personality Inventory (NPI) has been loaded in the workspace as a dataframe named npi. Print the first five rows of this dataframe using the .head().

Which of these variables do you think might be associated?
'''

import pandas as pd
import codecademylib3

npi = pd.read_csv("npi_sample.csv")

print(npi.head())