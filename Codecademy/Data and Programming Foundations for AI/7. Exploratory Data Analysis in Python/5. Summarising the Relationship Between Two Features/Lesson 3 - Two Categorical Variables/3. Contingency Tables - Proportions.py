'''
In the previous exercise, we looked at an association between the influence and leader questions using a contingency table of frequencies. However, sometimes it’s helpful to convert those frequencies to proportions. We can accomplish this simply by dividing the all the frequencies in a contingency table by the total number of observations (the sum of the frequencies):

influence_leader_freq = pd.crosstab(npi.influence, npi.leader)
influence_leader_prop = influence_leader_freq/len(npi)
print(influence_leader_prop)

Copy to Clipboard

Output:

leader           no       yes
influence                    
no         0.271695  0.116518
yes        0.212670  0.399117
The resulting contingency table makes it slightly easier to compare the proportion of people in each category. For example, we see that the two largest proportions in the table (.399 and .271) are in the yes/yes and no/no cells of the table. We can also see that almost 40% of the surveyed population (by far the largest proportion) both see themselves as leaders and think they have a talent for influencing people.

Instructions
Checkpoint 1 Passed
1.
The contingency table of frequencies for special (whether or not a person sees themself as “special”) and authority (whether or not a person likes to have authority) is saved for you as special_authority_freq.

Convert this table of frequencies to a table of proportions and save the result as special_authority_prop, then print it out.
'''


import pandas as pd
import numpy as np

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq / len(npi)

# print out special_authority_prop
print(special_authority_prop)