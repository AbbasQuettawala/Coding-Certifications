'''
In the previous exercise we calculated the following marginal proportions for the leader and influence questions:

leader            influence
no     0.484      no     0.388
yes    0.516      yes    0.612
In order to understand whether these questions are associated, we can use the marginal proportions to create a contingency table of expected proportions if there were no association between these 
Preview: Docs Loading link description
variables
. To calculate these expected proportions, we need to multiply the marginal proportions for each combination of categories:

leader = no	leader = yes
influence = no	0.484*0.388 = 0.188	0.516*0.388 = .200
influence = yes	0.484*0.612 = 0.296	0.516*0.612 = 0.315
These proportions can then be converted to frequencies by multiplying each one by the sample size (11097 for this data):

leader = no	leader = yes
influence = no	0.188*11097 = 2087	0.200*11097 = 2221
influence = yes	0.296*11097 = 3288	0.315*11097 = 3501
This table tells us that if there were no association between the leader and influence questions, we would expect 2087 people to answer no to both.

In python, we can calculate this table using the chi2_contingency() function from SciPy, by passing in the observed frequency table. There are actually four outputs from this function, but for now, we’ll only look at the fourth one:

from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(influence_leader_freq)
print(np.round(expected))

Copy to Clipboard

Output:

[[2087. 2221.]
 [3288. 3501.]]
Note that the ScyPy function returned the same expected frequencies as we calculated “by hand” above! Now that we have the expected contingency table if there’s no association, we can compare it to our observed contingency table:

leader       no   yes
influence            
no         3015  1293
yes        2360  4429
The more that the expected and observed tables differ, the more sure we can be that the variables are associated. In this example, we see some pretty big differences (eg., 3015 in the observed table compared to 2087 in the expected table). This provides additional evidence that these variables are associated.

Instructions
Checkpoint 1 Passed
1.
The contingency table of frequencies for the special and authority questions is saved for you in script.py as special_authority_freq.

Use the chi2_contingency() function to calculate the expected frequency table for these two questions if there were no association. Save the result as expected.

Checkpoint 2 Passed
2.
Use np.round() to print out the expected contingency table, with values rounded to the nearest whole number. Compare this to the observed frequency table. How much do the numbers in these tables differ?
'''


import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print("observed contingency table:")
print(special_authority_freq)

# calculate the expected contingency table if there's no association and save it as expected
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)

# print out the expected frequency table
print("expected contingency table (no association):")
print(np.round(expected))