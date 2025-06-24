'''
Examining the relationship between 
Preview: Docs Loading link description
variables
 can give us key insight into our data. In this lesson, we will cover ways of assessing the association between a quantitative variable and a categorical variable.

In the next few exercises, we’ll explore a dataset that contains the following information about students at two portuguese schools:

school: the school each student attends, Gabriel Periera ('GP') or Mousinho da Silveria ('MS')
address: the location of the student’s home ('U' for urban and 'R' for rural)
absences: the number of times the student was absent during the school year
Mjob: the student’s mother’s job industry
Fjob: the student’s father’s job industry
G3: the student’s score on a math assessment, ranging from 0 to 20
Suppose we want to know: Is a student’s score (G3) associated with their school (school)? If so, then knowing what school a student attends gives us information about what their score is likely to be. For example, maybe students at one of the schools consistently score higher than students at the other school.

To start answering this question, it is useful to save scores from each school in two separate lists:

scores_GP = students.G3[students.school == 'GP']
scores_MS = students.G3[students.school == 'MS']

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
The dataset described above has been saved for you in the workspace as a Pandas dataframe named students. Inspect the first five rows of students using the .head() method. Take a look at the other columns. Which are categorical and which are quantitative?

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Suppose that we want to know whether there is an association between student math scores (G3) and the student’s address (urban or rural). Separate out G3 scores into two separate lists: one for students who live in an urban location ('U') and one for students who live in a rural location ('R'). Name these lists scores_urban and scores_rural.
'''

import numpy as np
import pandas as pd
import codecademylib3

students = pd.read_csv('students.csv')

#print the first five rows of students:
print(students.head())


#separate out scores for students who live in urban and rural locations:
scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']