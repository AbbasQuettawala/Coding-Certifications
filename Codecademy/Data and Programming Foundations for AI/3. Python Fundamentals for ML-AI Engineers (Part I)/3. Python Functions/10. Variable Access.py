"""
As we expand our programs with more functions, we might start to ponder, where exactly do we have access to our variables? To examine this, let’s revisit a modified version of the first function we built out together:

def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")

Copy to Clipboard

What if we wanted to access the variable destination outside of the function? Could we use it? Take a second to think about what the following program will output, then check the result below!

def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")

print(destination)

Copy to Clipboard

Output Results

We call the part of a program where destination can be accessed its 
Preview: Docs Loading link description
scope
. The scope of destination is only inside the trip_welcome().

Take a look at another example:

budget = 1000

# Here we are using a default value for our parameter of `destination` 
def trip_welcome(destination="California"):
    print(" Looks like you're going to " + destination)
    print(" Your budget for this trip is " + str(budget))

print(budget)
trip_welcome()

Copy to Clipboard

Our output would be:

1000
Looks like you're going to California 
Your budget for this trip is 1000

Copy to Clipboard

Here we are able to access the budget both inside the trip_welcome function as well as our print() statement. If a variable lives outside of any function it can be accessed anywhere in the file.

We will be exploring the concept of scope more after this entire lesson but for now, let’s play around!

Note: Working with multiple functions can be a bit overwhelming at first. Don’t hesitate to use hints or even look at the solution code if you get stuck.

Instructions
Checkpoint 1 Enabled
1.
Our users want to be able to save a list of their favorite places in our travel application.

We have received a rough draft for this implementation from another coder, but there are some problems with variable scope which prevent it from working properly.

Take a second to understand what the program is doing and then hit Run the code to see the error.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Looking at the error, it seems like the main issue is that favorite_locations is not defined. Why would our program not be able to see our beautiful favorite_locations variable?

Aha! It must be a scope issue. Fix the scope of favorite_locations so that both our functions can access it.

Traceback (most recent call last):
  File "travel.py", line 11, in <module>
    show_favorite_locations()
  File "travel.py", line 8, in show_favorite_locations
    print("Your favorite locations are: " + favorite_locations)
NameError: name 'favorite_locations' is not defined
"""
# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"
def print_count_locations():
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()
