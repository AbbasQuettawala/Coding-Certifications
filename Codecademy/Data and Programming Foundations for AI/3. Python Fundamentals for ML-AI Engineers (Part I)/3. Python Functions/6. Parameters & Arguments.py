"""
Let’s return to our trip_welcome() function one more time! Let’s modify our function to give a welcome that is a bit more detailed.

def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to Times Square today.")

trip_welcome()

Copy to Clipboard

This will output:

Welcome to Tripcademy!
Looks like you're going to Times Square today.

Copy to Clipboard

Our function does a really good job of welcoming anyone who is traveling to Times Square but a really poor job if they are going anywhere else. In order for us to make our function a bit more dynamic, we are going to use the concept of function 
Preview: Docs Loading link description
parameters
.

Function parameters allow our function to accept data as an input value. We list the parameters a function takes as input between the parentheses of a function ( ).

Here is a function that defines a single parameter:

def my_function(single_parameter)
  # some code

Copy to Clipboard

In the context of our trip_welcome() function, it would look like this:

def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

Copy to Clipboard

In the above example, we define a single parameter called destination and apply it in our function body in the second print statement. We are telling our function it should expect some data passed in for destination that it can apply to any statements in the function body.

But how do we actually use this parameter? Our parameter of destination is used by passing in an argument to the function when we call it.

trip_welcome("Times Square")

Copy to Clipboard

This would output:

Welcome to Tripcademy!
Looks like you're going to Times Square today. 

Copy to Clipboard

To summarize, here is a quick breakdown of the distinction between a parameter and an argument:

The parameter is the name defined in the parenthesis of the function and can be used in the function body.
A function definition in Python

The argument is the data that is passed in when we call the function, which is then assigned to the parameter name.
Calling a function with a specific value like trip_welcome("Empire State Building")

Let’s write a function with parameters and call the function with an argument to see it all in action!

Instructions
Checkpoint 1 Enabled
1.
We want to create a program that allows our users to generate the directions for their upcoming trip!

Create a function called generate_trip_instructions() that defines one parameter called location.

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t worry, we will be filling in the code in the next step.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
generate_trip_instructions() should print out the following:

Looks like you are planning a trip to visit <location>

Copy to Clipboard

Where <location> will represent the location parameter.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
generate_trip_instructions() should also let our users know they can reach their location using public transit.

Let’s have generate_trip_instructions()also print out the following on a new line:

You can use the public subway system to get to <location>

Copy to Clipboard

Where <location> will represent the location parameter.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Time for some greenery! Let’s see what happens when we call the function and input the argument "Central Park", a backyard wonder in the heart of New York City.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
The day trip is over and we need to get back to the train station to head home. Change the argument to "Grand Central Station" and call the function again.

What changed in the output?

"""
# Your code below:

# Checkpoints 1, 2, & 3
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

# Checkpoints 4 & 5
#generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")