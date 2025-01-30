"""
When we have a bunch of data, we often want to calculate aggregate statistics (mean, standard deviation, median, percentiles, etc.) over certain subsets of the data.

Suppose we have a grade book with columns student, assignment_name, and grade. The first few lines look like this:

student	assignment_name	grade
Amy	Assignment 1	75
Amy	Assignment 2	35
Bob	Assignment 1	99
Bob	Assignment 2	35
…		
We want to get an average grade for each student across all assignments. We could do some sort of loop, but Pandas gives us a much easier option: the method .groupby.

For this example, we’d use the following command:

grades = df.groupby('student').grade.mean()


The output might look something like this:

student	grade
Amy	80
Bob	90
Chris	75
…	
In general, we use the following syntax to calculate aggregates:

df.groupby('column1').column2.measurement()


where:

column1 is the column that we want to group by ('student' in our example)
column2 is the column that we want to perform a measurement on (grade in our example)
measurement is the measurement function we want to apply (mean in our example)
For more on the groupby method, review the pandas documentation.

Instructions
Checkpoint 1 Enabled
1.
Let’s return to our orders data from ShoeFly.com.

In the previous exercise, our finance department wanted to know the most expensive shoe that we sold.

Now, they want to know the most expensive shoe for each shoe_type (i.e., the most expensive boot, the most expensive ballet flat, etc.).

Save your answer to the variable pricey_shoes.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Examine the object that you just created using:

print(pricey_shoes)


Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
What type of object is pricey_shoes?

Enter the following code to check:

print(type(pricey_shoes))

"""
import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes))

