"""
In Python, there are 3 different types of arguments we can give a function.

Positional arguments: arguments that can be called by their position in the function definition.

Keyword arguments: arguments that can be called by their name.

Default arguments: arguments that are given default values.

Positional Arguments are arguments we have already been using! Their assignments depend on their positions in the function call. Let’s look at a function called calculate_taxi_price() that allows our users to see how much a taxi would cost to their destination 🚕.

def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

Copy to Clipboard

In this function, miles_to_travel is positioned as the first parameter, rate is positioned as the second parameter, and discount is the third. When we call our function, the position of the arguments will be mapped to the positions defined in the function declaration.

# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)

Copy to Clipboard

Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call. Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.

calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

Copy to Clipboard

Lastly, sometimes we want to give our function parameters default values. We can provide a default value to a parameter by using the assignment operator (=). This will happen in the function declaration rather than the function call.

Here is an example where the discount argument in our calculate_taxi_price function will always have a default value of 10:

def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

Copy to Clipboard

When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:

# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)

Copy to Clipboard

Let’s practice using these different types of arguments!

Instructions
Checkpoint 1 Enabled
1.
Tripcademy (our trusty travel app) needs to allow passengers to plan a trip (duh).

Write a function called trip_planner() that will have three parameters: first_destination, second_destination and final_destination.

Give the final_destination parameter a default value of "Codecademy HQ".

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t worry, we will be filling in the code in the next step.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
First, we want to introduce the trip to users. Use print() in our function to output Here is what your trip will look like!.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
In our function definition let’s provide an itinerary that will describe the destinations our user will visit in order. Print a statement that follows this form:

First, we will stop in <first_destination>, then <second_destination>, and lastly <final_destination>

Copy to Clipboard

An example call to our function using positional arguments:

trip_planner("London", "India", "New Zealand")

Copy to Clipboard

Should output:

Here is what your trip will look like!
First, we will stop in London, then India, and lastly New Zealand

Copy to Clipboard

To test out your function, call trip_planner() with the following values for the parameters:

first_destination: "France"

second_destination: "Germany"

final_destination: "Denmark"

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Call the function trip_planner() again with the following values for the parameters:

first_destination: "Denmark"

second_destination: "France"

final_destination: "Germany"

Note the difference in your output depending on the position of your arguments.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
Call the function trip_planner() again but this time include the keyword arguments (e.g. first_destination) and put them in this exact order:

first_destination = "Iceland"

final_destination = "Germany"

second_destination = "India"

Checkpoint 6 Step instruction is unavailable until previous steps are completed
6.
Lastly, go ahead and call the function trip_planner() using only two positional arguments to see the default argument in action:

first_destination: "Brooklyn"

second_destination: "Queens"
"""

# Write your code below:
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):

  print("Here is what your trip will look like!")

  print(f"First we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")

trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")

trip_planner("Brooklyn", "Queens")