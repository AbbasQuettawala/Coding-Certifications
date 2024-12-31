"""
If you haven’t written Python before, you can still do this exercise even though it might feel a little like magic. Follow along and it will become clearer later on (we promise it isn’t magic!).

While JSON is a great universal format for data interchange, it might not be the ideal format in other aspects, such as readability. Instead, having the data in a tabular format (like a CSV) can make it much more human-readable and accessible. Therefore, being able to convert between file types is essential.

There are several libraries in Python to work with different data formats. For example, to convert the Census data from JSON to CSV, we can use the built-in csv library:

import csv

Copy to Clipboard

As a refresher, visit https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:* in your browser to view the total commuters count for all states.

The JSON data we got from the Census API is a list of 
Preview: Docs Loading link description
lists
 in Python, where each inner list corresponds to a single row of data. To convert from JSON to CSV, we want to write each sublist as a comma-separated row of data to file. This bit of code is a little complicated. We will use the writerows() method from the csv library:

with open('census.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r.json())

Copy to Clipboard

What is that code doing?
We first make a variable and call it file. Then we use 
Preview: Docs Used for opening files in a Python program.
open()
 to open a file, since we are going to write that file, we open it with mode='w' for writing mode. The newline='' ensures that newlines are always interpreted correctly.

Next, we use the writer() function from the csv library to make a writer object (don’t worry about what this is right now). We then use the writerows() method to write each row of data into comma-separated format.

Instructions
Checkpoint 1 Enabled
1.
Start by importing the csv module.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Use the .json() method to access the decoded JSON data and store it in a variable called r_json.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
We created an empty commute_data.csv file for you. Click on the tab above the code editor to see it.

Now write the JSON data into a CSV file called commute_data.csv

After you write the data to the file, click on the file again to see it filled with your data.
"""
import requests
import csv


r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')
r_json = r.json()

with open('commute_data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r.json())