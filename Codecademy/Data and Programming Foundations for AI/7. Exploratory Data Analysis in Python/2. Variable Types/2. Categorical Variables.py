"""
Categorical Variables
9 min
Without getting too philosophical about it, “your mind is a categorization machine” - HBR. We move through the world by categorizing things into various groups: safe/unsafe, best/worst, on/off. These categorizations help us process information. They also create major problems for us when we over-categorize, and can lead to bias and unfair assumptions.

However, we still do it, and regardless of the dangers, categorization helps us transform the world around us into data. (Being aware of the dangers is a crucial part of data analysis, but outside the scope of this lesson.)

Categorical variables come in 3 types:

Nominal variables, which describe something,
Ordinal variables, which have an inherent ranking, and
Binary variables, which have only two possible variations.
one box with 'Nominal variables' written in it and 3 boxes blow it with 'Nominal', 'Ordinal', and 'Binary' below, illustrating the relationship between each of these types of variables and nominal variables

Let’s look at each one separately

Nominal Variables
When we want to describe something about the world, we need a nominal variable. Nominal variables are usually words (i.e., red, yellow, blue or hot, cold), but they can also be numbers (i.e., zip codes or user id’s).

Often, nominal variables describe something with a lot of variation. It can be hard to capture all of that variation, so an ‘Other’ category is often necessary. For example, in the case of color, we could have a lot of different labels, but might still need an ‘Other’ category to capture anything we missed.

Ordinal variables
When our categories have an inherent order, we need an ordinal variable. Ordinal variables are usually described by numbers like 1st, 2nd, 3rd. Places in a race, grades in school, and the scales in survey responses (Likert Scales) are ordinal variables.

Ordinal variables can be a little tricky because even though they are numbers, it doesn’t make sense to do math on them. For example, let’s say an Olympian won a Gold medal (1st place) and a Bronze medal (3rd place). We wouldn’t say that they averaged Silver medals (2nd place).

Though there is some debate about whether Likert scales should be treated like intervals or ordinal categories, most statisticians agree that they are ordinal categories and therefore should not be summarized numerically.

Binary variables
When there are only two logically possible variations, we need a binary variable. Binary variables are things like on/off, yes/no, and TRUE/FALSE. If there is any possibility of a third option, it is not a binary variable.

Let’s take a look at our cereal dataset.

print(cereal.head())


id	name	mfr	type	fiber	rating	shelf	vitamins	coupons	price
0	22341	100% Bran…	Nestle	C	10.0	68.40	top	25	4	3.46
1	22791	100% Natur…	Quaker Oats	C	2.0	33.98	top	0	1	3.36
2	98141	All-Bran…	Kelloggs	C	9.0	59.43	top	25	4	2.07
3	20001	All-Bran w…	Kelloggs	C	14.0	93.70	top	25	3	3.57
4	67121	Almond Del…	Ralston P..	C	1.0	34.38	top	25	1	5.21

There are some obvious categorical variables: The name of the product, the mfr (manufacturer), and the shelf are all nominal categorical variables. We know this because they are written in descriptive words or letters.

A little less obvious is the type field. They are all ‘C’, which could be a ranking (A, B, C, and therefore an ordinal variable) or it could be a description and therefore a nominal variable. We would have to return to the data dictionary to find out for certain.

The id field may also cause confusion. It’s a number, but it’s not a count or a measurement. Rather, ‘id’ is a categorical variable since it is describing each observation in the same way that the name is.

Let’s go over our Netflix dataset to get a little more practice working with categorical variables.

Instructions
Checkpoint 1 Enabled
1.
Run the code in the workspace to view the first five rows of the movies dataframe.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Print the unique values of the country column to assess its variable type.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Identify whether the country column is ordinal or nominal and assign the value of country_variable_type to either 'ordinal', 'nominal', or 'binary'.
"""
import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the unique values in the country column
print(movies['country'].unique())


# Set the correct value for country_variable_type
country_variable_type = 'nominal'
