'''
Recall that in the last exercise, we began investigating whether or not there is an association between math scores and the school a student attends. We can begin quantifying this association by using two common summary statistics, mean and median differences. To calculate the difference in mean G3 scores for the two schools, we can start by finding the mean math score for students at each school. We can then find the difference between them:

mean_GP = np.mean(scores_GP)
mean_MS = np.mean(scores_MS)
print(mean_GP) #output: 10.49
print(mean_MS) #output: 9.85
print(mean_GP - mean_MS) #Output: 0.64

Copy to Clipboard

We see that the mean math score for students at GP is 10.49, while the mean score for students at MS is 9.85. The mean difference is 0.64. We can follow a similar process to calculate a median difference:

median_GP = np.median(scores_GP)
median_MS = np.median(scores_MS)
print(median_GP) #Output: 11.0
print(median_MS) #Output: 10.0
print(median_GP-median_MS) #Output: 1.0

Copy to Clipboard

GP students also have a higher median score, by one point. Highly associated 
Preview: Docs Loading link description
variables
 tend to have a large mean or median difference. Since “large” could have different meanings depending on the variable, we will go into more detail in the next exercise.

Instructions
Checkpoint 1 Passed
1.
Your lists from the previous exercise (scores_urban and scores_rural) have been created for you in script.py. Use these lists to calculate the mean score for both groups. Store the results as scores_urban_mean and scores_rural_mean, respectively.

Checkpoint 2 Passed
2.
Calculate the mean difference between the two groups and save the result as mean_diff. Based on this number, do you think the variables are associated? Why or why not?

Checkpoint 3 Passed
3.
Use the lists to calculate the median score for both groups. Store the results as scores_urban_median, scores_rural_median, respectively. Print out the result of each variable.

Checkpoint 4 Passed
4.
Calculate the median difference between the two groups, save the result as median_diff. Based on this value, do you think the variables are associated? Why or why not?
'''


import numpy as np
import pandas as pd
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#calculate means for each group:
scores_urban_mean = np.mean(scores_urban)
scores_rural_mean = np.mean(scores_rural)

#print mean scores:
print('Mean score - students w/ urban address:')
print(scores_urban_mean)
print('Mean score - students w/ rural address:')
print(scores_rural_mean)

#calculate mean difference:
mean_diff = scores_urban_mean - scores_rural_mean

#print mean difference
print('Mean difference:')
print(mean_diff)

#calculate medians for each group:
scores_urban_median = np.median(scores_urban)
scores_rural_median = np.median(scores_rural)

#print median scores
print('Median score - students w/ urban address:')
print(scores_urban_median)
print('Median score - students w/ rural address:')
print(scores_rural_median)

#calculate median difference
median_diff = scores_urban_median - scores_rural_median

#print median difference
print('Median difference:')
print(median_diff)
