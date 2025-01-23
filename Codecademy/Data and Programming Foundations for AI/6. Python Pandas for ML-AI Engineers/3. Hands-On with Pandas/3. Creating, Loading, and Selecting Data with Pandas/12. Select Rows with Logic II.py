"""
You can also combine multiple logical statements, as long as each statement is in parentheses.

For instance, suppose we wanted to select all rows where the customer’s age was under 30 or the customer’s name was “Martha Jones”:

name	address	phone	age
Martha Jones	123 Main St.	234-567-8910	28
Rose Tyler	456 Maple Ave.	212-867-5309	22
Donna Noble	789 Broadway	949-123-4567	35
Amy Pond	98 West End Ave.	646-555-1234	29
Clara Oswald	54 Columbus Ave.	714-225-1957	31
…			

We could use the following code:

df[(df.age < 30) |
   (df.name == 'Martha Jones')]


In Python, | means “or” and & means “and”.

Instructions
Checkpoint 1 Enabled
1.
You want to see how the number of clinic visits changed between March and April.

Create the variable march_april, which contains the data from March and April. Do this using two logical statements combined using |, which means “or”.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Inspect march_april using print.
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

march_april = df[(df.month == 'March') | (df.month == 'April')]
print(march_april)