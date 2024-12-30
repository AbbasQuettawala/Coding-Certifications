"""
Just as we learned to insert elements at specific indices, Python gives us a method to remove elements at a specific index using a method called .pop().

The 
Preview: Docs Removes an item from a list while also returning it.
.pop()
 method takes an optional single input:

The index for the element you want to remove.
To see it in action, let’s consider a list called cs_topics that stores a collection of topics one might study in a computer science program.

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

Copy to Clipboard

Two of these topics don’t look like they belong, let’s see how we remove them using .pop().

First let’s remove "Clowns 101":

removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)

Copy to Clipboard

Would output:

['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
'Clowns 101'

Copy to Clipboard

Notice two things about this example:

The method can be called without a specific index. Using .pop() without an index will remove whatever the last element of the list is. In our case "Clowns 101" gets removed.

.pop() is unique in that it will return the value that was removed. If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method. In this case, we assigned it to removed_element.

Lastly let’s remove "Balloon Making":

cs_topics.pop(2)
print(cs_topics)

Copy to Clipboard

Would output:

['Python', 'Data Structures', 'Algorithms']

Copy to Clipboard

Notice two things about this example:

The method can be called with an optional specific index to remove. In our case, the index 2 removes the value of "Balloon Making".
We don’t have to save the removed value to any variable if we don’t care to use it later.
Note: Passing in an index that does not exist or calling .pop() on an empty list will both result in an IndexError.

Let’s apply what we learned about the .pop() method.

Instructions
Checkpoint 1 Enabled
1.
We have decided to pursue the study of data science in addition to our computer science coursework. We signed up for an online school that would help us become proficient.

Check out the current list of topics we will be studying in our code editor.

Click Run to print out the list.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
It looks like we have an overlap with our computer science curriculum for the topic of "Python 3".

Let’s remove the topic from the list of data_science_topics using our newly learned .pop() method.

Print data_science_topics to see your result.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Looks like there is overlap on the "Algorithms" topic as well. Let’s use .pop() to remove it as well.

Print data_science_topics to see the changes.
"""

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)
data_science_topics.pop(3)
print(data_science_topics)