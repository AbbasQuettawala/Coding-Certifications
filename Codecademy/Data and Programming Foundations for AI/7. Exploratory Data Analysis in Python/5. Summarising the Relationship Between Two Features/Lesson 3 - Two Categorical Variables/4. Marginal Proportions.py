'''
In the previous exercises, we looked at an association between the influence and leader questions using a contingency table. We saw some evidence of an association between these questions.

Now, let’s take a moment to think about what the tables would look like if there were no association between the 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
. Our first instinct may be that there would be .25 (25%) of the data in each of the four cells of the table, but that is not the case. Let’s take another look at our contingency table.

leader           no       yes
influence                    
no         0.271695  0.116518
yes        0.212670  0.399117
We might notice that the bottom row, which corresponds to people who think they have a talent for influencing people, accounts for 0.213 + 0.399 = 0.612 (or 61.2%) of surveyed people — more than half! This means that we can expect higher proportions in the bottom row, regardless of whether the questions are associated.

The proportion of respondents in each category of a single question is called a marginal proportion. For example, the marginal proportion of the population that has a talent for influencing people is 0.612. We can calculate all the marginal proportions from the contingency table of proportions (saved as influence_leader_prop) using row and column sums as follows:

leader_marginals = influence_leader_prop.sum(axis=0)
print(leader_marginals)
influence_marginals =  influence_leader_prop.sum(axis=1)
print(influence_marginals)

Copy to Clipboard

Output:

leader
no     0.484365
yes    0.515635
dtype: float64

influence
no     0.388213
yes    0.611787
dtype: float64
While respondents are approximately split on whether they see themselves as a leader, more people think they have a talent for influencing people than not.

Instructions
Checkpoint 1 Passed
1.
The solution code from the previous exercise has been provided in script.py to create a contingency table of proportions (saved as special_authority_prop) for the special and authority columns. Use this to calculate the marginal proportions for the authority variable and save the result as authority_marginals.

Print out authority_marginals. Do more people like to have authority over people or not?

Checkpoint 2 Passed
2.
Use special_authority_prop to calculate the marginal proportions for the special variable and save the result as special_marginals.

Print out special_marginals. Do more people see themselves as special or not special?
'''


import pandas as pd
import numpy as np

npi = pd.read_csv("npi_sample.csv")

# save the table of frequencies as special_authority_freq:
special_authority_freq = pd.crosstab(npi.special, npi.authority)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq/len(npi)

# calculate and print authority_marginals
authority_marginals = special_authority_prop.sum(axis=0)
print(authority_marginals)

# calculate and print special_marginals
special_marginals = special_authority_prop.sum(axis=1)
print(special_marginals)
