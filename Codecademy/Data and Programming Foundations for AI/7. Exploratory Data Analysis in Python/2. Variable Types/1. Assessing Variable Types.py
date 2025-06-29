"""
Assessing Variable Types
7 min
“It all began with a variable”, the storyteller began.

Just kidding, no one starts their stories that way, even though variables are where all data stories begin.

Variables define datasets. They are the characteristics or attributes that we evaluate during data collection. There are two ways to do that evaluation: we can measure or we can categorize.

How we evaluate determines what kind of variable we have. Since there are only two ways to get data, there are only two types of variables: numerical and categorical.

A box labeled "Variables" points to two boxes below labeled "Categorical" and "Quantitative"

Every observation (the individuals or objects we are collecting data about) is classified according to its characteristics. In “flat” file formats (like tables, csvs, or DataFrames), the observations are the rows, the variables are the columns, and the values are at the intersection.

We’ll go deeper into categorical and numerical variables in the following exercises.

Typically, the best way to understand your data is to look at a sample of it.

In the example dataset about cereal below, we can look at the first few rows with the .head() method to get an idea of the variable types that we have.

print(cereal.head())


id	name	mfr	type	fiber	rating	shelf	vitamins	coupons	price
0	22341	100% Bran…	Nestle	C	10.0	68.40	top	25	4	3.46
1	22791	100% Natur…	Quaker Oats	C	2.0	33.98	top	0	1	3.36
2	98141	All-Bran…	Kelloggs	C	9.0	59.43	top	25	4	2.07
3	20001	All-Bran w…	Kelloggs	C	14.0	93.70	top	25	3	3.57
4	67121	Almond Del…	Ralston P..	C	1.0	34.38	top	25	1	5.21

There are several types of variables. For example:

The price column describes how much the cereal costs. We don’t know if that’s how much the consumer pays or the grocer pays, but we can be fairly sure that it’s a numerical variable.

In the mfr column, there are labels like Nestle, Quaker Oats, and Kelloggs, which seem like brands. Since brands are categories, mfr is most likely a categorical variable.

The id column also has numbers, but we can assume that since it’s the id, it’s not actually representing a value. It’s probably the label for the observation. Since it’s a label, even though it’s a number, id is a categorical variable.

If we were downloading this from a data repository, we would expect a data dictionary to define these variables and validate (or invalidate) our assumptions.

It is still important to inspect our dataset because it gives us a better understanding of the data that we are working with and the kinds of operations that will be possible.

Let’s practice inspecting a dataset to identify its variable types.

This dataset is a modified version of this Netflix data. The est_budget (USD) and cast_count variables were created for illustration purposes.

Instructions
Checkpoint 1 Enabled
1.
The movies dataframe is composed of the television shows and movies hosted on the Netflix platform in 2019. Print the first five rows of the dataframe using the .head() method.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
The rating variable describes the Motion Picture Association Film Rating Board rating for each film and the TV Parental Guidelines Monitoring Board rating for each television show. We have consolidated the ratings for simplicity.

Inspect the first five rows that were just printed out from the .head() method. Identify whether the rating variable is quantitative or categorical and assign the value of 'numerical' or 'categorical' to a variable called rating_variable_type.
"""
import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv", index_col=0)

# View the first five rows of the dataframe


# Set the correct value for rating_variable_type
rating_variable_type = None
print(rating_variable_type)

print(movies.head())

rating_variable_type = 'categorical'