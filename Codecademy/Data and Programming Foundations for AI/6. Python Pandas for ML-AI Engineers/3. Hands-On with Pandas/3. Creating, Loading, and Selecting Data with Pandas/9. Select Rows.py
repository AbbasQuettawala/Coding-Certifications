"""
Let’s revisit our orders from ShoeFly.com:

id	first_name	last_name	email	shoe_type	shoe_material	shoe_color
54791	Rebecca	Lindsay	RebeccaLindsay57@hotmail.com	clogs	faux-leather	black
53450	Emily	James	EmilyJames25@gmail.com	ballet flats	faux-leather	navy
91987	Joyce	Waller	Joyce.Waller@gmail.com	sandals	fabric	black
14437	Justin	Erickson	Justin.Erickson@outlook.com	clogs	faux-leather	red
…						

Maybe our Customer Service department has just received a message from Joyce Waller, so we want to know exactly what she ordered. We want to select this single row of data.

DataFrames are zero-indexed, meaning that we start with the 0th row and count up from there. Joyce Waller’s order is the 2nd row.

We select it using the following command:

orders.iloc[2]


When we select a single row, the result is a Series (just like when we select a single column).

Instructions
Checkpoint 1 Enabled
1.
You’re getting ready to staff the clinic for March this year. You want to know how many visits took place in March last year, to help you prepare.

Write a command that will produce a Series made up of the March data from df from all four clinic sites and save it to the variable march.
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

march = df.iloc[2]