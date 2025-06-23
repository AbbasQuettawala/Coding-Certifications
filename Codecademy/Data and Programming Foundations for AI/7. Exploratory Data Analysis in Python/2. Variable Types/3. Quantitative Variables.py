"""
Quantitative Variables
7 min
“One accurate measurement is worth a thousand expert opinions”

– Grace Hopper

Numerical variables are created two ways: through measurement and counting. While measurement is a matter of philosophical debate, counting is pretty straightforward. The result is continuous and discrete variables.

one box labeled 'Numerical' with two boxes below it labeled 'Continous' and 'Discrete' to represent the relationship between the three terms

Continuous variables come from measurements. For a variable to be continuous, there must be infinitely smaller units of measurement between one unit and the next unit. Continuous variables can be represented by decimal places (but because of rounding, sometimes they are whole numbers). Length, time, and temperature are all good examples of continuous variables because they all increase continuously.

Discrete variables come from counting. For a variable to be discrete, there must be gaps between the smallest possible units. People, cars, and dogs are all good examples of discrete variables.

Some variables depend on context to determine if they are continuous or discrete. Money and time can both be measured continuously or discretely.

For money, all currencies have a smallest-possible-unit (i.e., the cent in USD) and are therefore discrete. However, banks and other institutions sometimes measure money in fractions of a cent, treating it like a continuous variable.

It is therefore always essential to understand how your data was created in order to represent it appropriately.

Let’s take a look at the cereal dataset again.

id	name	mfr	type	fiber	rating	shelf	vitamins	coupons	price
0	22341	100% Bran…	Nestle	C	10.0	68.40	top	25	4	3.46
1	22791	100% Natur…	Quaker Oats	C	2.0	33.98	top	0	1	3.36
2	98141	All-Bran…	Kelloggs	C	9.0	59.43	top	25	4	2.07
3	20001	All-Bran w…	Kelloggs	C	14.0	93.70	top	25	3	3.57
4	67121	Almond Del…	Ralston P..	C	1.0	34.38	top	25	1	5.21

There are five numerical variables: fiber, rating, vitamins, coupons, and price.

Without looking at the data dictionary, we can make some guesses about what kind of numerical variables they are:

Fiber, rating, and price all have decimal places. That’s our first clue that they might be continuous. Based on our limited knowledge, we might guess that fiber and rating are both continuous measurements that could have more decimal places, and price is discrete because there’s nothing smaller than a cent.

Vitamins and coupons do not have decimal places. Vitamins and coupons both seem like good candidates to be counts and therefore discrete. The answers to “how many vitamins” and “how many coupons” would both be whole numbers. (We already said that ID is categorical in the last exercise)

We would be more confident in our answers if we were able to inspect the documentation. But sometimes documentation isn’t available and you have to take your best guess.

Let’s try it out on our Netflix data.

Instructions
Checkpoint 1 Enabled
1.
Run the code in the workspace to view the first five rows of the movies dataframe.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
The release_year variable expresses the year that a movie or television show was originally released. Inspect the first five rows of the dataset that were printed, and identify whether this column is discrete or continuous. From this inspection, assign the value of release_year_variable_type to either 'discrete' or 'continuous'.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
The cast_count variable describes how many cast members are in the show. Inspect the first five rows of the printed dataset, and identify whether this column is discrete or continuous. From this inspection, assign the value of cast_count_variable_type to either 'discrete' or 'continuous'.
"""

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Set the correct value for release_year_variable_type
release_year_variable_type = 'discrete'
print(release_year_variable_type)

# Set the correct value for duration_variable_type
cast_count_variable_type = 'discrete'
print(cast_count_variable_type)