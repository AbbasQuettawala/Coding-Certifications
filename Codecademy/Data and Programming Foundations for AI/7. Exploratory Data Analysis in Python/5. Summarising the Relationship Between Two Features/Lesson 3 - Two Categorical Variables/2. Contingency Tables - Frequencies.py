'''
Contingency tables, also known as two-way tables or cross-tabulations, are useful for summarizing two 
Preview: Docs Loading link description
variables
 at the same time. For example, suppose we are interested in understanding whether there is an association between influence (whether a person thinks they have a talent for influencing people) and leader (whether they see themself as a leader). We can use the crosstab function from pandas to create a contingency table:

influence_leader_freq = pd.crosstab(npi.influence, npi.leader)
print(influence_leader_freq)

Copy to Clipboard

Output:

leader       no   yes
influence            
no         3015  1293
yes        2360  4429
This table tells us the number of people who gave each possible combination of responses to these two questions. For example, 2360 people said that they do not see themselves as a leader but have a talent for influencing people.

To assess whether there is an association between these two variables, we need to ask whether information about one variable gives us information about the other. In this example, we see that among people who don’t see themselves as a leader (the first column), a larger number (3015) don’t think they have a talent for influencing people. Meanwhile, among people who do see themselves as a leader (the second column), a larger number (4429) do think they have a talent for influencing people.

So, if we know how someone responded to the leadership question, we have some information about how they are likely to respond to the influence question. This suggests that the variables are associated.

Instructions
Checkpoint 1 Passed
1.
Do you think there will be an association between special (whether or not a person sees themself as “special”) and authority (whether or not a person likes to have authority)? Create a contingency table for these two variables and store the table as special_authority_freq, then print out the result.

Based on this table, do you think the variables are associated?
'''


import pandas as pd
import codecademylib3

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print(special_authority_freq)