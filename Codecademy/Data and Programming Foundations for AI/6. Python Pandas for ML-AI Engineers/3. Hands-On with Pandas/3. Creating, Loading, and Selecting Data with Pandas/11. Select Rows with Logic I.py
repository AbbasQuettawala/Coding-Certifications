"""
You can select a subset of a DataFrame by using logical statements:

df[df.MyColumnName == desired_column_value]


We have a large DataFrame with information about our customers. A few of the many rows look like this:

name	address	phone	age
Martha Jones	123 Main St.	234-567-8910	28
Rose Tyler	456 Maple Ave.	212-867-5309	22
Donna Noble	789 Broadway	949-123-4567	35
Amy Pond	98 West End Ave.	646-555-1234	29
Clara Oswald	54 Columbus Ave.	714-225-1957	31
…	…	…	…

Suppose we want to select all rows where the customer’s age is 30. We would use:

df[df.age == 30]


In Python, == is how we test if a value is exactly equal to another value.

We can use other logical statements, such as:

Greater Than, > — Here, we select all rows where the customer’s age is greater than 30:
df[df.age > 30]


Less Than, < — Here, we select all rows where the customer’s age is less than 30:
df[df.age < 30]


Not Equal, != — This snippet selects all rows where the customer’s name is not Clara Oswald:
df[df.name != 'Clara Oswald']


Instructions
Checkpoint 1 Enabled
1.
You’re going to staff the clinic for January of this year. You want to know how many visits took place in January of last year, to help you prepare.

Create variable january using a logical statement that selects the row of df where the 'month' column is 'January'.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Inspect january using print.
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
           'clinic_west'])

january = df[df.month == 'January']
print(january)