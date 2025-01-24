"""
In Pandas, we often use lambda functions to perform complex operations on columns. For example, suppose that we want to create a column containing the email provider for each email address in the following table:

Name	Email
JOHN SMITH	john.smith@gmail.com
Jane Doe	jdoe@yahoo.com
joe schmo	joeschmo@hotmail.com
We could use the following code with a lambda function and the string method .split():

df['Email Provider'] = df.Email.apply(
    lambda x: x.split('@')[-1]
    )


The result would be:

Name	Email	Email Provider
JOHN SMITH	john.smith@gmail.com	gmail.com
Jane Doe	jdoe@yahoo.com	yahoo.com
joe schmo	joeschmo@hotmail.com	hotmail.com
Instructions
Checkpoint 1 Enabled
1.
Create a lambda function get_last_name which takes a string with someone’s first and last name (i.e., John Smith), and returns just the last name (i.e., Smith).

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
The DataFrame df represents the hours worked by different employees over the course of the week. It contains the following columns:

'name': The employee’s name
'hourly_wage': The employee’s hourly wage
'hours_worked': The number of hours worked this week
Use the lambda function get_last_name to create a new column last_name with only the employees’ last name.
"""

import codecademylib3
import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda x: x.split(' ')[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)
