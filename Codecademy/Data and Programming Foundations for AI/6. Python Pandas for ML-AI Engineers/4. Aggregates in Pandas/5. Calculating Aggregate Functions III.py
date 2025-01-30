"""
Sometimes, the operation that you want to perform is more complicated than mean or count. In those cases, you can use the apply method and lambda functions, just like we did for individual column operations. Note that the input to our lambda function will always be a list of values.

A great example of this is calculating percentiles. Suppose we have a DataFrame of employee information called df that has the following columns:

id: the employee’s id number
name: the employee’s name
wage: the employee’s hourly wage
category: the type of work that the employee does
Our data might look something like this:

id	name	wage	category
10131	Sarah Carney	39	product
14189	Heather Carey	17	design
15004	Gary Mercado	33	marketing
11204	Cora Copaz	27	design
…			
If we want to calculate the 75th percentile (i.e., the point at which 75% of employees have a lower wage and 25% have a higher wage) for each category, we can use the following combination of apply and a lambda function:

# np.percentile can calculate any percentile over an array of values
high_earners = df.groupby('category').wage
    .apply(lambda x: np.percentile(x, 75))
    .reset_index()


The output, high_earners might look like this:

category	wage
0	design	23
1	marketing	35
2	product	48
…		
Instructions
Checkpoint 1 Enabled
1.
Once more, we’ll return to the data from ShoeFly.com. Our Marketing team says that it’s important to have some affordably priced shoes available for every color of shoe that we sell.

Let’s calculate the 25th percentile for shoe price for each shoe_color to help Marketing decide if we have enough cheap shoes on sale. Save the data to the variable cheap_shoes.

Note: Be sure to use reset_index() at the end of your query so that cheap_shoes is a DataFrame.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Display cheap_shoes using print.
"""

import codecademylib3
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()
print(cheap_shoes)