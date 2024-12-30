"""
Let’s return to our classroom heights example:

heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]

Copy to Clipboard

Two-dimensional lists can be accessed similar to their one-dimensional counterpart. Instead of providing a single pair of brackets [ ] we will use an additional set for each dimension past the first.

If we wanted to access "Noelle"‘s height:

#Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)

Copy to Clipboard

Would output:

61

Copy to Clipboard

Here are the index numbers to access data for the list heights:

Element	Index
"Noelle"	heights[0][0]
61	heights[0][1]
"Ali"	heights[1][0]
70	heights[1][1]
"Sam"	heights[2][0]
67	heights[2][1]

Let’s practice accessing data in a two-dimensional list.

Instructions
Checkpoint 1 Enabled
1.
We want to have a way to store all of our classroom test score data.

Using the provided table, create a two-dimensional list called class_name_test to represent the data. Each sublist in class_name_test should have one student’s name and their associated score.

Name	Test Score
"Jenny"	90
"Alexus"	85.5
"Sam"	83
"Ellie"	101.5

Print class_name_test to see the result.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Use double square brackets ([][]) to select Sam‘s test score from the list class_name_test.

Save it to the variable sams_score.

Print the variable sams_score to see the result.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Use double square brackets ([][]) to select Ellies test score from the list class_name_test. This time only use negative indices!

Save it to the variable ellies_score.

Print the variable ellies_score to see the result.
"""

#Your code below:
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)