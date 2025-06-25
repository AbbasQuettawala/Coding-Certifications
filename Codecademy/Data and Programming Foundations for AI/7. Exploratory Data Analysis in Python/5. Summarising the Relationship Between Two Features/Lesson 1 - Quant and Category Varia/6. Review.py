'''
In this lesson, we used summary statistics and data visualization tools to examine an association between a quantitative and categorical variable. More specifically, we:

evaluated mean and median differences
inspected side-by-side box plots
examined overlapping histograms
looked at pair-wise comparisons for a quantitative and a non-binary categorical variable
After calculating a mean or median difference and visually comparing distributions, the next step might be to run a hypothesis test to look for evidence of population-level differences (will a similar difference in scores be observed for ALL students who ever attend these schools?). Now that you know how to investigate whether 
Preview: Docs Loading link description
variables
 are associated, you can use these techniques to explore associations on more datasets.

Note that data in this lesson was downloaded from the UCI Machine Learning repository:

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [archive.ics.uci.edu/ml/index.php]. Irvine, CA: University of California, School of Information and Computer Science.

The data was originally collected by:

P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto, Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7.

Instructions
A new dataset named titanic has been uploaded for you in script.py. This data contains information about passengers on the Titanic, including the amount they paid for their fare and whether or not they survived (note: this is a subset of the full data available). To practice the skills learned in this lesson, let’s investigate whether there is an association between the fare that a passenger paid (Fare) and whether or not they survived (Survived, which is equal to 0 if the passenger died and 1 if they survived):

Calculate the difference in mean fare paid by those who survived and those who died. Which group paid a higher average fare?
Calculate the difference in median fare for those who survived and those who died.
Create side-by-side box plots of fares by survival. Now that you can see the spread of the data, do the mean/median differences seem relatively small or large?
Create overlapping histograms of fares by survival (you’ll have to delete or comment out your box plot code before you try to make a histogram). Does this provide any additional information?
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3

titanic = pd.read_csv('titanic.csv')

print(titanic.head())

#separate out fares by survival
fares_died = titanic.Fare[titanic.Survived == 0]
fares_survived = titanic.Fare[titanic.Survived == 1]

#mean difference
mean_fare_died = np.mean(fares_died)
mean_fare_surv = np.mean(fares_survived)
mean_diff = mean_fare_surv-mean_fare_died
print('mean difference: ')
print(mean_diff)

#median difference
med_fare_died = np.median(fares_died)
med_fare_surv = np.median(fares_survived)
med_diff = med_fare_surv-med_fare_died
print("median difference: ")
print(med_diff)

#create subplots (scroll to see plots)
fig = plt.figure(figsize = (10,20))

#create the boxplot:
ax = fig.add_subplot(2,1,1)
ax = sns.boxplot(data = titanic, x = 'Survived', y = 'Fare')

#create the histograms:
ax = fig.add_subplot(2,1,2)
ax = plt.hist(fares_died, color="blue", label="Died", normed=True, alpha=0.5)
ax = plt.hist(fares_survived, color="red", label="Survived", normed=True, alpha=0.5)
ax = plt.legend()
plt.show()