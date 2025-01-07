"""
When we read a file, we might want to grab the whole document in a single string, like 
Preview: Docs Allows the user to read the contents of an open file and return the number of associated bytes.
.read()
 would return. But what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line instead of having the whole thing. Suppose we have a file:

keats_sonnet.txt

To one who has been long in city pent,
’Tis very sweet to look into the fair
And open face of heaven,—to breathe a prayer
Full in the smile of the blue firmament.

Copy to Clipboard

script.py

with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)

Copy to Clipboard

The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt. It then iterates over each line in the document and prints the entire file out.

Instructions
Checkpoint 1 Enabled
1.
Using a with statement, create a file object pointing to the file how_many_lines.txt. Store that file object in the variable lines_doc.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Iterate through each of the lines in lines_doc.readlines() using a for loop.

Inside the for loop print out each line of how_many_lines.txt.
"""
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)