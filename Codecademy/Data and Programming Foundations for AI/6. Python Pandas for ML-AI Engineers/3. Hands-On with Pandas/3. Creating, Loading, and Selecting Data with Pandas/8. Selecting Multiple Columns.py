"""
When you have a larger DataFrame, you might want to select just a few columns.

For instance, let’s return to a DataFrame of orders from ShoeFly.com:

id	first_name	last_name	email	shoe_type	shoe_material	shoe_color
54791	Rebecca	Lindsay	RebeccaLindsay57@hotmail.com	clogs	faux-leather	black
53450	Emily	Joyce	EmilyJoyce25@gmail.com	ballet flats	faux-leather	navy
91987	Joyce	Waller	Joyce.Waller@gmail.com	sandals	fabric	black
14437	Justin	Erickson	Justin.Erickson@outlook.com	clogs	faux-leather	red

We might just be interested in the customer’s last_name and email. We want a DataFrame like this:

last_name	email
Lindsay	RebeccaLindsay57@hotmail.com
Joyce	EmilyJoyce25@gmail.com
Waller	Joyce.Waller@gmail.com
Erickson	Justin.Erickson@outlook.com

To select two or more columns from a DataFrame, we use a list of the column names. To create the DataFrame shown above, we would use:

new_df = orders[['last_name', 'email']]


Note: Make sure that you have a double set of brackets ([[]]), or this command won’t work!

Instructions
Checkpoint 1 Enabled
1.
Now, you want to compare visits to the Northern and Southern clinics.

Create a variable called clinic_north_south that contains ONLY the data from the columns clinic_north and clinic_south.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
When we select multiple columns, do we get a Series or a DataFrame?

After you’ve created the variable, enter the command:

print(type(clinic_north_south))


to see what data type you’ve created.

How is this different from what happened in the previous exercise?
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
clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))

