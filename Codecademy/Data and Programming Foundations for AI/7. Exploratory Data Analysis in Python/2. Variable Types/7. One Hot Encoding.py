'''
In the previous exercise, we saw how label encoding can be useful for ordinal categorical variables. But sometimes we need a different approach. This could be because:

We have a nominal categorical variable (like breed of dog), so it doesn’t really make sense to assign numbers like 0,1,2,3,4,5 to our categories, as this could create an order among the species that is not present.

We have an ordinal categorical variable but we don’t want to assume that there’s equal spacing between categories.

Another way of encoding categorical variables is called One-Hot Encoding (OHE). With OHE, we essentially create a new binary variable for each of the categories within our original variable. This technique is useful when managing nominal variables because it encodes the variable without creating an order among the categories.

Let’s take a look at the titanic dataframe.

Survived	Pclass	Name	SibSp	Parch	Fare	Cabin	Embarked
0	0	3	Braund, Mr. Owen Harris	1	0	7.2500	NaN	S
1	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th…	1	0	71.2833	C85	C
2	1	3	Heikkinen, Miss. Laina	0	0	7.9250	NaN	S
3	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	1	0	53.1000	C123	S
4	0	3	Allen, Mr. William Henry	0	0	8.0500	NaN	S

To perform OHE on a variable within a pandas dataframe, we can use the pandas .get_dummies() method which creates a binary or “dummy” variable for each category. We can assign the columns to be encoded in the columns parameter, and set the data parameter to the dataset we intend to alter. The pd.get_dummies() method will also work on data types other than category.

Tables illustrating how pd.get_dummies encodes a variable named Education which contains categories labeled "high school diploma," "associates," "bachelors," and "post doctorate". In this example, we create a binary ("dummy") variable for each of these categories. For "high school diploma," we create "Ed_high_dip." For "associates," we create "Ed_associates." For "bachelors," we create "Ed_bachelors." Finally, for "post doctorate," we create "Ed_post_doc." The resulting dataframe has these for "dummy" variables as columns, which are each labeled 0 or 1.

Notice that when using pd.get_dummies(), we are effectively creating a new dataframe that contains a different set of variables to the original dataframe.

titanic = pd.get_dummies(data=titanic, columns=['Embarked'])
print(titanic.head())

Copy to Clipboard

Survived	Pclass	Name	SibSp	Parch	Fare	Cabin	Embarked_C	Embarked_Q	Embarked_S
1	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th…	1	0	71.2833	C85	1	0	0
3	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	1	0	53.1000	C123	0	0	1
6	0	1	McCarthy, Mr. Timothy J	0	0	51.8625	E46	0	0	1
10	1	3	Sandstrom, Miss. Marguerite Rut	1	1	16.7000	G6	0	0	1
11	1	1	Bonnell, Miss. Elizabeth	0	0	26.5500	C103	0	0	1

By passing in the dataset and column that we want to encode into pd.get_dummies(), we have created a new dataframe that contains three new binary variables with values of 1 for True and 0 for False, which we can view when we scroll to the right in the table. Now we haven’t assigned weighting to our nominal variable. It is important to note that OHE works best when we do not create too many additional variables, as increasing the dimensionality of our dataframe can create problems when working with certain machine learning models.

Instructions
Checkpoint 1 Passed
1.
Run the code in the workspace to view the first five rows of the cereal dataframe.

Checkpoint 2 Passed
2.
One-Hot Encode the mfr variable with pd.get_dummies().

Checkpoint 3 Passed
3.
Check the new variables by printing the first five rows of the cereal dataframe. Make sure to scroll to the right to view all of the variables.
'''

import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
cereal = pd.read_csv('cereal.csv', index_col=0)

# Show the first five rows of the `cereal` dataframe
print(cereal.head())

# Create a new dataframe with the `mfr` variable One-Hot Encoded
cereal = pd.get_dummies(data=cereal, columns=['mfr'])

# Show first five rows of new dataframe
print(cereal.head())