"""
Now we know how to create and load data. Let’s select parts of those datasets that are interesting or important to our analyses.

Suppose you have the DataFrame called customers, which contains the ages of your customers:

name	age
Rebecca Erikson	35
Thomas Roberson	28
Diane Ochoa	42
…	…

Perhaps you want to take the average or plot a histogram of the ages. In order to do either of these tasks, you’d need to select the column.

There are two possible syntaxes for selecting all values from a column:

Select the column as if you were selecting a value from a dictionary using a key. In our example, we would type customers['age'] to select the ages.
If the name of a column follows all of the rules for a variable name (doesn’t start with a number, doesn’t contain spaces or special characters, etc.), then you can select it using the following notation: df.MySecondColumn. In our example, we would type customers.age.
When we select a single column, the result is called a Series.

Instructions
Checkpoint 1 Enabled
1.
The DataFrame df represents data collected by four health clinics run by the same organization. Each row represents a month from January through June and shows the number of appointments made at four different clinics.

You want to analyze what’s been happening at the North location. Create a variable called clinic_north that contains ONLY the data from the column clinic_north.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
What exactly have you selected?

After you create the variable, enter the command:

print(type(clinic_north))


to see what data type you’ve created.

How is this different from what you get if you type the following?


"""

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df.clinic_north
# or clinic_north = df['clinic_north']

print(type(clinic_north))
print(type(df))