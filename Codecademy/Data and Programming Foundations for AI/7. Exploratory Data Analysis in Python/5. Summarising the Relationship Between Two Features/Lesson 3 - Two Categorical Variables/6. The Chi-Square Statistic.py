'''
In the previous exercise, we calculated a contingency table of expected frequencies if there were no association between the leader and influence questions. We then compared this to the observed contingency table. Because the tables looked somewhat different, we concluded that responses to these questions are probably associated.

While we can inspect these tables visually, many data scientists use the Chi-Square statistic to summarize how different these two tables are. To calculate the Chi Square statistic, we simply find the squared difference between each value in the observed table and its corresponding value in the expected table, and then divide that number by the value from the expected table; finally add up those numbers:

C
h
i
S
q
u
a
r
e
=
∑
(
o
b
s
e
r
v
e
d
−
e
x
p
e
c
t
e
d
)
2
e
x
p
e
c
t
e
d
ChiSquare= 
∑
​
  
expected
(observed−expected) 
2
 
​
 
The Chi-Square statistic is also the first output of the SciPy function chi2_contingency():

from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(influence_leader_freq)
print(chi2)
output: 1307.88

Copy to Clipboard

The interpretation of the Chi-Square statistic is dependent on the size of the contingency table. For a 2x2 table (like the one we’ve been investigating), a Chi-Square statistic larger than around 4 would strongly suggest an association between the 
Preview: Docs Loading link description
variables
. In this example, our Chi-Square statistic is much larger than that — 1307.88! This adds to our evidence that the variables are highly associated.

Instructions
Checkpoint 1 Passed
1.
The contingency table of frequencies for the special and authority questions is saved for you in script.py as special_authority_freq.

Use the chi2_contingency() function to calculate Chi-Square statistic for these two variables. Save the result as chi2 and print it out. Do these variables appear to be associated?
'''
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)

# calculate the chi squared statistic and save it as chi2, then print it:
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)
print(chi2)
