"""
When we perform a groupby across multiple columns, we often want to change how our data is stored. For instance, recall the example where we are running a chain of stores and have data about the number of sales at different locations on different days:

Location	Date	Day of Week	Total Sales
West Village	February 1	W	400
West Village	February 2	Th	450
Chelsea	February 1	W	375
Chelsea	February 2	Th	390
We suspected that there might be different sales on different days of the week at different stores, so we performed a `groupby` across two different columns (`Location` and `Day of Week`). This gave us results that looked like this:
Location	Day of Week	Total Sales
Chelsea	M	300
Chelsea	Tu	310
Chelsea	W	375
Chelsea	Th	390
…		
West Village	Th	450
West Village	F	390
West Village	Sa	250
…		
In order to test our hypothesis, it would be more useful if the table was formatted like this:
Location	M	Tu	W	Th	F	Sa	Su
Chelsea	300	310	375	390	300	150	175
West Village	300	310	400	450	390	250	200
…							
Reorganizing a table in this way is called pivoting. The new table is called a pivot table.

In Pandas, the command for pivot is:

df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')


For our specific example, we would write the command like this:

# First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')


Just like with groupby, the output of a pivot command is a new DataFrame, but the indexing tends to be “weird”, so we usually follow up with .reset_index().

For more on the pivot function, see the pandas documentation.

Instructions
Checkpoint 1 Enabled
1.
In the previous example, you created a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased for ShoeFly.com.

The purchasing manager complains that this DataFrame is confusing.

Make it easier for her to compare purchases of different shoe colors of the same shoe type by creating a pivot table. Save your results to the variable shoe_counts_pivot.

Your table should look like this:

shoe_type	black	brown	navy	red	white
ballet flats	…	…	…	…	…
sandals	…	…	…	…	…
stilettos	…	…	…	…	…
wedges	…	…	…	…	…
Remember to use reset_index() at the end of your code!

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Display shoe_counts_pivot using print.
"""

import codecademylib3
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
shoe_counts_pivot = shoe_counts.pivot(columns = 'shoe_color', index = 'shoe_type', values = 'id').reset_index()
print(shoe_counts_pivot)