'''

In script.py, the data has been subsetted for you into two smaller datasets: games from 2010 (named nba_2010) and games from 2014 (named nba_2014). To start, let’s focus on the 2010 data.

Suppose you want to compare the knicks to the nets with respect to points earned per game. Using the pts column from the nba_2010 DataFrame, create two series named knicks_pts_10 (fran_id = "Knicks") and nets_pts_10(fran_id = "Nets") that represent the points each team has scored in their games.

2.
Calculate the difference between the two teams’ average points scored and save the result as diff_means_2010. Based on this value, do you think fran_id and pts are associated? Why or why not?

3.
Rather than comparing means, it’s useful look at the full distribution of values to understand whether a difference in means is meaningful. Create a set of overlapping histograms that can be used to compare the points scored for the Knicks compared to the Nets. Use the series you created in the previous step (1) and the code below to create the plot. Do the distributions appear to be the same?

4.
Now, let’s compare the 2010 games to 2014. Replicate the steps from the previous three exercises using nba_2014. First, calculate the mean difference between the two teams points scored. Save and print the value as diff_means_2014. Did the difference in points get larger or smaller in 2014? Then, plot the overlapping histograms. Does the mean difference you calculated make sense?

5.
For the remainder of this project, we’ll focus on data from 2010. Let’s now include all teams in the dataset and investigate the relationship between franchise and points scored per game.

Using nba_2010, generate side-by-side boxplots with points scored (pts) on the y-axis and team (fran_id) on the x-axis. Is there any overlap between the boxes? Does this chart suggest that fran_id and pts are associated? Which pairs of teams, if any, earn different average scores per game?

Analyzing relationships between Categorical variables
6.
We’d like to know if teams tend to win more games at home compared to away.

The variable game_result indicates whether a team won a particular game ('W' stands for “win” and 'L' stands for “loss”). The variable game_location indicates whether a team was playing at home or away ('H' stands for “home” and 'A' stands for “away”).

Data scientists will often calculate a contingency table of frequencies to help them determine if categorical variables are associated. Calculate a table of frequencies that shows the counts of game_result and game_location.

Save your result as location_result_freq and print your result. Based on this table, do you think the variables are associated?

7.
Convert this table of frequencies to a table of proportions and save the result as location_result_proportions. Print your result.

8.
Using the contingency table we created in Task 6 (use the counts – NOT the proportions), calculate the expected contingency table (if there were no association) and the Chi-Square statistic and print your results. Does the actual contingency table look similar to the expected table — or different? Based on this output, do you think there is an association between these variables?

Analyzing Relationships Between Quantitative Variables
9.
For each game, 538 has calculated the probability that each team will win the game. We want to know if teams with a higher probability of winning (according to 538) also tend to win games by more points.

In the data, 538’s prediction is saved as forecast. The point_diff column gives the margin of victory/defeat for each team (positive values mean that the team won; negative values mean that they lost).

Using nba_2010, calculate the covariance between forecast (538’s projected win probability) and point_diff (the margin of victory/defeat) in the dataset. Call this point_diff_forecast_cov. Save and print your result. Looking at the matrix, what is the covariance between these two variables?

10.
Because 538’s forecast variable is reported as a probability (not a binary), we can calculate the strength of the correlation.

Using nba_2010, calculate the correlation between forecast and point_diff. Call this point_diff_forecast_corr. Save and print your result. Does this value suggest an association between the two variables?

11.
Generate a scatter plot of forecast (on the x-axis) and point_diff (on the y-axis). Does the correlation value make sense?
'''


import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

# Step 1 - Comparing knicks and Nets
knicks_pts_10 = nba_2010.pts[nba.fran_id=='Knicks']
nets_pts_10 = nba_2010.pts[nba.fran_id=='Nets']

# Step 2 
knicks_mean_score = np.mean(knicks_pts_10) # Mean of Knicks Scores
nets_mean_score = np.mean(nets_pts_10) # Mean of Nets Scores
diff_means = knicks_mean_score - nets_mean_score


# Step 3
plt.hist(knicks_pts_10, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()
plt.close()

# Step 4
knicks_pts_10_2014 = nba_2014.pts[nba.fran_id=='Knicks']
nets_pts_10_2014 = nba_2014.pts[nba.fran_id=='Nets']

knicks_mean_score_2014 = np.mean(knicks_pts_10_2014) # Mean of Knicks Scores
nets_mean_score_2014 = np.mean(nets_pts_10_2014) # Mean of Nets Scores
diff_means_2014 = knicks_mean_score_2014 - nets_mean_score_2014

plt.hist(knicks_pts_10_2014, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts_10_2014, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.title("2014 Season")
plt.show()

# Step 5
plt.clf() #to clear the previous plot
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.show()

# Step 6
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)


# step 7
location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)


# Step 8
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)


# Step 9 
forecast = nba_2010['forecast']
point_diff = nba_2010['pts'] - nba_2010['opp_pts']
point_diff_forecast_cov = np.cov(forecast, point_diff)
print(point_diff_forecast_cov)

# Step 10
point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

# Step 11
plt.clf() #to clear the previous plot
plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()




