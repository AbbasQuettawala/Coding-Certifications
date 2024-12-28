"""
Excellent work! 👏 In this lesson, you’ve covered a major fundamental programming concept used in the majority of all programs to organize code into reusable blocks. To recap, we explored:

What problems arise in our programs without functions
What 
Preview: Docs Loading link description
functions
 are and how to write them
How whitespace plays an important role in how a program will execute our code and more importantly distinguish function code from non-function code
How to pass input values into our functions using parameters and arguments
The difference between built-in and user-defined functions and some common 
Preview: Docs Loading link description
built-in functions
 python offers
How we can reuse function output with the return keyword, as well as multiple returns.
Where 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
 can be accessed in our programs that use functions
Let’s practice putting all these concepts together!

Instructions
Checkpoint 1 Enabled
1.
Alright, this is it. We are going to use all of our knowledge of functions to build out TripPlanner V1.0.

First, like in our previous exercises, we want to make sure to welcome our users to the application.

Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this:

Welcome to tripplanner v1.0 <Name Here>

Copy to Clipboard

Where <Name Here> represents the parameter variable of name we defined.

Call trip_planner_welcome(), passing your name as an argument.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user’s trip.

An example call for this function will look like this:

estimated_time_rounded(2.5)

Copy to Clipboard

Where 2 represents 2 hours and .5 represents 30 minutes.

Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:

Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
Return rounded_time.
After the function definition, call estimated_time_rounded() with a decimal argument and save the result to a variable called estimate. Since this amount represents a time, be sure to use a positive number.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Next, we are going to generate messages for a user’s planned trip.

Create a function called destination_setup() that will have four parameters in this exact order:

origin
destination
estimated_time
mode_of_transport
Give the parameter mode_of_transport a default value of "Car". The program will error out if we run it since we have not defined a function body yet. Don’t worry we will do that in the next step.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Next, we are going to write four print() statements in our function. The output on this function call should look like this:

Your trip starts off in <origin>
And you are traveling to <destination>
You will be traveling by <mode_of_transport>
It will take approximately <estimated_time> hours

Copy to Clipboard

Each of these print() statements use a different parameter from our function destination_setup().

Note: The estimated_time parameter will come in the form of an integer. Make sure to use str() to convert the parameter in your print statement.

After the function definition, call destination_setup() with the following arguments:

origin and destination should be string values representing the places you will travel from and to
Use the estimate you created earlier for estimated_time
If you will be traveling by a mode other than Car, be sure to overwrite the default value of mode_of_transport
Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
Great job! 👏

We have successfully finished our first version of the trip builder application. Go ahead and try passing different values into your functions!
"""

# Write your code below:

def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome(" <YOUR NAME HERE> ")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")


destination_setup(" Home ", " Pizza place ", estimate, "Car")