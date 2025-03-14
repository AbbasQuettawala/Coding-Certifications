"""
Now that we’ve practiced defining a function, let’s learn about calling a function to execute the code within its body.

The process of executing the code inside the body of a function is known as calling it (This is also known as “executing a function”). To call a function in Python, type out its name followed by parentheses ( ).

Let’s revisit our directions_to_timesSq() function :

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")

Copy to Clipboard

To call our function, we must type out the function’s name followed by a pair of parentheses and no indentation:

directions_to_timesSq()

Copy to Clipboard

Calling the function will execute the print statements within the body (from the top statement to the bottom statement) and result in the following output:

Walk 4 mins to 34th St Herald Square train station.
Take the Northbound N, Q, R, or W train 1 stop.
Get off the Times Square 42nd Street stop.

Copy to Clipboard

Note that you can only call a function after it has been defined in your code.

Now it’s your turn to call a function!

Instructions
Checkpoint 1 Enabled
1.
Call the directions_to_timesSq() function.

Click Run to see it execute and print out.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Add an additional print statement to our directions_to_timesSq() function.

Have the statement print "Take lots of pictures!"

Run your code again and see how your output changes.
"""
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Call your function here:
directions_to_timesSq()
