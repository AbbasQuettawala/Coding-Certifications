"""
In this project, you will examine how factors such as age, sex, number of children, and smoking status contribute to medical insurance costs.

You will apply your knowledge of Python control flow to write code that gives people advice on how to lower their medical insurance costs.

Let’s get started!

Tasks
7/7 complete
Mark the tasks as complete by checking them off
Intro to Control Flow
1.
First, take a look at the code in script.py.

The function estimate_insurance_cost() estimates the medical insurance cost for an individual, based on four variables:

age: age of the individual in years
sex: 0 for female, 1 if male
num_of_children: number of children the individual has
smoker: 0 for a non-smoker, 1 for a smoker
These variables are used in the following formula to estimate an individual’s insurance cost:

i
n
s
u
r
a
n
c
e
_
c
o
s
t
=
4
0
0
∗
a
g
e
−
1
2
8
∗
s
e
x
+
4
2
5
∗
n
u
m
_
o
f
_
c
h
i
l
d
r
e
n
+
1
0
0
0
0
∗
s
m
o
k
e
r
−
2
5
0
0
insurance_cost=400∗age
−128∗sex+425∗num_of_children
+10000∗smoker−2500
​
 
Click “Save” to see the estimated medical insurance cost for Keanu, a 29 year-old male smoker with three children.

2.
Currently, our function prints out the estimated insurance cost based on the values passed into the function. But it doesn’t do much beyond that.

It would be much more helpful if our function could provide more insight into how we can lower our insurance cost. We’ll learn to do exactly that by using control flow – if, elif, and else statements – in our code.

When you’re ready, move on to the next step.

Analyzing Smoker Status
3.
In general, insurance costs are higher for smokers. We can use data from the smoker variable to provide advice on how to lower insurance costs.

Let’s create a function that analyzes an individual’s smoking status.

At the top of your code, define a function called analyze_smoker() that takes an input smoker_status. For now, the function should print smoker_status.

4.
Inside of the analyze_smoker() function, replace the print statement you wrote in the previous step with an if/else statement that does the following:

If smoker_status is equal to 1, print "To lower your cost, you should consider quitting smoking."
Otherwise, print "Smoking is not an issue for you."
5.
Now that we’ve written the analyze_smoker() function, let’s make use of it.

In the estimate_insurance_cost() function, go to the line of code that prints the estimated insurance cost. On the next line, make a function call to analyze_smoker(), passing in the smoker variable as an argument.

Click “Save” to see the result.

Analyze your own insurance cost
6.
Now that we’ve estimated and analyzed Keanu’s insurance cost, let’s see if we can do the same for our own!

At the bottom of your code, create a new insurance cost variable for yourself, similar to how we did it for Keanu.

Set the variable equal to a function call to estimate_insurance_cost(), passing in your own age, sex, number of children, and smoker status.

Click “Save” to see the result. Do you see any ways that you can potentially lower your insurance cost?

Extra
7.
Great job! In this project, you used control flow in your code – using if, elif, and else statements – to provide advice on how individuals can lower their medical insurance costs.

As a data scientist, it’s important to have an understanding of control flow as you’ll eventually work with and build complex decision tree algorithms. You are now better equipped to move forward in your data science journey!

If you’d like additional practice on control flow, feel free to experiment with ways you might extend this project!

Happy coding!
"""

# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

my_insurance_cost = estimate_insurance_cost(name = 'Abbas', age = 21, sex = 1, num_of_children = 0, smoker = 0)