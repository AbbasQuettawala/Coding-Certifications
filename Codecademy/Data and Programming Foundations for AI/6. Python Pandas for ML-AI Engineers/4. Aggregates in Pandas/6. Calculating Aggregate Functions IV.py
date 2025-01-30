"""
Sometimes, we want to group by more than one column. We can easily do this by passing a list of column names into the groupby method.

Imagine that we run a chain of stores and have data about the number of sales at different locations on different days:

Location	Date	Day of Week	Total Sales
West Village	February 1	W	400
West Village	February 2	Th	450
Chelsea	February 1	W	375
Chelsea	February 2	Th	390
We suspect that sales are different at different locations on different days of the week. In order to test this hypothesis, we could calculate the average sales for each store on each day of the week across multiple months. The code would look like this:

df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()


The results might look something like this:

Location	Day of Week	Total Sales
Chelsea	M	402.50
Chelsea	Tu	422.75
Chelsea	W	452.00
…		
West Village	M	390
West Village	Tu	400
…		
Instructions
Checkpoint 1 Enabled
1.
At ShoeFly.com, our Purchasing team thinks that certain shoe_type/shoe_color combinations are particularly popular this year (for example, blue ballet flats are all the rage in Paris).

Create a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased. Save it to the variable shoe_counts.

You should be able to do this using groupby and count().

Note: When we’re using count(), it doesn’t really matter which column we perform the calculation on. You should use id in this example, but we would get the same answer if we used shoe_type or last_name.

Remember to use reset_index() at the end of your code!

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Display shoe_counts using print.
"""

import codecademylib3
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

print(shoe_counts)