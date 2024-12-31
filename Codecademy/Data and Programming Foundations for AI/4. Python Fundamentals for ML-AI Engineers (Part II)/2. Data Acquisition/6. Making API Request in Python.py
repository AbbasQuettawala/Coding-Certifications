"""
Now that you have a pretty good idea of how the Census Data API works, let’s take a look at how to pull the data in Python. Begin by importing the requests library with this command:

import requests

Copy to Clipboard

Next, we can use the get() method to return the data from our desired URL:

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*') 

Copy to Clipboard

The result is a response object (just like in the last exercise), but this time we stored it in a variable named r.

We can look at that response data by using the .text attribute. The text attribute turns the data into a string.

We can also use the .json() method that can automatically decode JSON data into the appropriate Python object. This is useful when working with JSON data, as in the case of the Census API, to have the data in a more intuitive data structure.

# Access data as JSON string
print(r.text)
 
# Access decoded JSON data as Python object
print(r.json())

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
Start by importing the requests module.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Make a GET request to the Census API to request county-level data containing

the NAME variable,
the total commuters count, and
the count for commuters who travel 90 or more minutes
for all counties
within the state of New York.
(see the previous exercise for this URL)

Store the response object in a variable called r.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Use the .text attribute to access the returned string data and store it in a variable called r_text.

Try printing r_text with the print(___) command.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Use the .json() method to access the decoded JSON data and store it in a variable called r_json. Try printing out r_json.

Can you see the advantage working with r_json has over r_text?
"""
import requests
r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')
r_text = r.text
print(r.text)
r_json = r.json()
print(r_json)