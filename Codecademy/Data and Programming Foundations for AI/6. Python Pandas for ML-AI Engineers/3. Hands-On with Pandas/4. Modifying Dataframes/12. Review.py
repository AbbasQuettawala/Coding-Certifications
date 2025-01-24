"""
Great job! In this lesson, you learned how to modify an existing 
Preview: Docs Loading link description
DataFrame
. Some of the skills you’ve learned include:

Adding columns to a DataFrame
Using lambda functions to calculate complex quantities
Renaming columns
Let’s practice what you just learned!

Instructions
Checkpoint 1 Enabled
1.
Once more, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store.

More messy order data has been loaded into the variable orders. Examine the first 5 rows of the data using print and .head().

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Many of our customers want to buy vegan shoes (shoes made from materials that do not come from animals). Add a new column called shoe_source, which is vegan if the materials is not leather and animal otherwise.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Our marketing department wants to send out an email to each customer. Using the columns last_name and gender create a column called salutation which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.

Here are some examples:

last_name	gender	salutation
Smith	male	Dear Mr. Smith
Jones	female	Dear Ms. Jones

"""

import codecademylib3
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)