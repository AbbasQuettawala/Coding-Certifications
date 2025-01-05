"""
You can get both the keys and the values with the 
Preview: Docs Returns a list of tuples for each key-value pair in a dictionary.
.items()
 method. Like 
Preview: Docs Returns a list of keys for a dictionary.
.keys()
 and 
Preview: Docs Loading link description
.values()
, it returns a dict_list object. Each element of the dict_list returned by .items() is a tuple consisting of:

(key, value)

Copy to Clipboard

so to iterate through, you can use this syntax:

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")

Copy to Clipboard

which would yield this output:

Apple has a value of 184 billion dollars.
Google has a value of 141.7 billion dollars.
Microsoft has a value of 80 billion dollars.
Coca-Cola has a value of 69.7 billion dollars.
Amazon has a value of 64.8 billion dollars.

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out a string that looks like:

Women make up [value] percent of [key]s.

"""
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for value, key in pct_women_in_occupation.items():
  print("Women make up " + str(key) + " percent of " + value + "s")