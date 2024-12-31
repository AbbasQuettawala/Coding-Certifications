"""
A while loop isn’t only good for counting! Similar to how we saw for loops working with lists, we can use while loops to iterate through a 
Preview: Docs Loading link description
list
 as well.

Let’s return to our ingredient list:

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

Copy to Clipboard

We know that while loops require some form of a variable to track the condition of the loop to start and stop.

Take some time to think about what we would use to track whether we need to start/stop the loop if we want to iterate through ingredients and print every element.

Click here to find out!

We can then use this length in addition to another variable to construct the while loop:

length = len(ingredients)
index = 0

while index < length:
  print(ingredients[index])
  index += 1

Copy to Clipboard

Let’s break this down:

# Length will be 5 in this case
length = len(ingredients)

Copy to Clipboard

Explanation

# Index starts at zero
index = 0

Copy to Clipboard

Explanation

while index < length:

Copy to Clipboard

Explanation

# The first iteration will print ingredients[0]
print(ingredients[index])

Copy to Clipboard

Explanation

# Increment index to access the next element in ingredients
# Each iteration gets closer to making the conditional no longer true
index += 1

Copy to Clipboard

Explanation

Our final output would be:

milk
sugar
vanilla extract
dough
chocolate

Copy to Clipboard

Let’s use a while loop to iterate through some lists!

Instructions
Checkpoint 1 Enabled
1.
We are going to write a while loop to iterate over the provided list python_topics.

First, we will need a variable to represent the length of the list. This will help us know how many times our while loop needs to iterate.

Create a variable length and set its value to be the length of the list of python_topics.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Next, we will require a variable to compare to our length variable to make sure we are able to implement a condition that eventually allows the loop to stop.

Create a variable called index and initialize the value to be 0.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Let’s now build our loop. We want our loop to iterate over the list of python_topics and on each iteration print "I am learning about <element from python_topics>". For this loop we will need the following components:

A condition for our while loop
A statement in the loop body to print from our condition
A statement in the loop body to increment our index forward.
The end result should output:

I am learning about variables
I am learning about control flow
I am learning about loops
I am learning about modules
I am learning about classes

Copy to Clipboard

If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise, you may have an infinite loop! If the stop condition for our loop is never met, we will create an infinite loop which stops our program from running anything else. To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.
"""
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)

index = 0

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1

