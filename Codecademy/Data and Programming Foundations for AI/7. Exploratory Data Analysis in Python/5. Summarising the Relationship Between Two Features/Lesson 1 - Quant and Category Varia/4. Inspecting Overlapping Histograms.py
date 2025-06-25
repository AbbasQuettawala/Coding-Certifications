'''
Another way to explore the relationship between a quantitative and categorical variable in more detail is by inspecting overlapping histograms. In the code below, setting alpha = .5 ensures that the histograms are see-through enough that we can see both of them at once. We have also used normed=True make sure that the y-axis is a density rather than a frequency (note: the newest version of matplotlib renamed this parameter density instead of normed):

plt.hist(scores_GP , color="blue", label="GP", normed=True, alpha=0.5)
plt.hist(scores_MS , color="red", label="MS", normed=True, alpha=0.5)
plt.legend()
plt.show()

Copy to Clipboard

title

By inspecting this histogram, we can clearly see that the entire distribution of scores at GP (not just the mean or median) appears slightly shifted to the right (higher) compared to the scores at MS. However, there is also still a lot of overlap between the scores, suggesting that the association is relatively weak.

Note that there are only 46 students at MS, but there are 349 students at GP. If we hadn’t used normed = True, our histogram would have looked like this, making it impossible to compare the distributions fairly:

title

While overlapping histograms and side by side boxplots can convey similar information, histograms give us more detail and can be useful in spotting patterns that were not visible in a box plot (eg., a bimodal distribution). For example, the following set of box plots and overlapping histograms illustrate the same hypothetical data:

title

While the box plots and means/medians appear similar, the overlapping histograms illuminate the differences between these two distributions of scores.

Instructions
Checkpoint 1 Passed
1.
Your lists from the previous exercise (scores_urban and scores_rural) have been created for you in script.py. Use them to create an overlaid histogram of scores for students who live in urban and rural locations.

Remember to use different colors for each histogram, set normed = True, alpha = 0.5, and use the labels 'Urban' and 'Rural', respectively.

Based on the overlaid histogram, do you think there is an association between these two variables?
'''


import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#create the overlapping histograms here:
plt.hist(scores_urban, color="blue", label = "urban", normed = True, alpha=0.5)
plt.hist(scores_rural, color="red", label = "rural", normed = True, alpha=0.5)
plt.legend()

plt.show()