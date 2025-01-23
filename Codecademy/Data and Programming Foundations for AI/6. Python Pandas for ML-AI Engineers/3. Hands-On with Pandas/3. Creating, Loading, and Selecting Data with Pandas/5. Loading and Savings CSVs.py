"""
When you have data in a CSV, you can load it into a 
Preview: Docs Loading link description
DataFrame
 in Pandas using 
Preview: Docs Loading link description
.read_csv()
:

pd.read_csv('my-csv-file.csv')


In the example above, the .read_csv() method is called. The CSV file called my-csv-file is passed in as an argument.

We can also save data to a CSV, using .to_csv().

df.to_csv('new-csv-file.csv')


In the example above, the .to_csv() method is called on df (which represents a DataFrame object). The name of the CSV file is passed in as an argument (new-csv-file.csv). By default, this method will save the CSV file in your current directory.

Instructions
Checkpoint 1 Enabled
1.
You’re working for the County of Whoville and you just received a CSV of data about the different cities in your county. Read the CSV 'sample.csv' into a variable called df, so that you can learn more about the cities.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Let’s inspect the CSV.

Type print(df) on the next line and then run your code. What sort of data were you sent?
"""
import codecademylib3
import pandas as pd

df = pd.read_csv('sample.csv')
print(df)