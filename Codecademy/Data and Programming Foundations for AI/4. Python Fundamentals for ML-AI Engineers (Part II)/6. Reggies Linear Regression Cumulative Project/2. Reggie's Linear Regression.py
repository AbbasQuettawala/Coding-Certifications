"""
Part 1: Calculating Error
1.
The line we will end up with will have a formula that looks like:

y = m*x + b


where m is the slope of the line and b is the intercept, where the line crosses the y-axis.

Create a function called get_y() that takes in m, b, and x. It should return what the y value would be for that x on that line!

Once you have defined get_y(), test it out by uncommenting the print() statements and checking if the expected values display in the terminal.

2.
Reggie wants to try a bunch of different m values and b values and see which line produces the least error. To calculate the error between a point and a line, he wants a function called calculate_error(), which will take in m, b, and an [x, y] point called point and return the distance between the line and the point.

First, define the function calculate_error(), passing m, b, and point as parameters.

3.
To find the distance:

Get the x-value from the point and store it in a variable called x_point
Get the y-value from the point and store it in a variable called y_point
Use get_y() to get the y-value that x_point would be on the line
Find the difference between the y from get_y() and y_point
Return the absolute value of the distance (you can use the built-in function abs() to do this)
The distance represents the error between the line y = m*x + b and the point given.

4.
We have provided several test cases for calculate_error(). Uncomment each print() statement and check to see that it displays the expected value.

5.
Great! Reggie’s datasets will be sets of points. For example, he ran an experiment comparing the width of bouncy balls to how high they bounce:

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]


The first datapoint, (1, 2), means that his 1cm bouncy ball bounced 2 meters. The 4cm bouncy ball bounced 4 meters.

As we try to fit a line to this data, we will need a function called calculate_all_error(), which takes m and b that describe a line, and points, a set of data like the example above.

calculate_all_error() should iterate through each point in points and calculate the error from that point to the line (using calculate_error()). It should keep a running total of the error, and then return that total after the loop.

6.
We have provided several test cases for calculate_all_error(). Uncomment each print() statement and check to see that it displays the expected value.

7.
Great! It looks like we now have a function that can take in a line and Reggie’s data and return how much error that line produces when we try to fit it to the data.

Our next step is to find the m and b that minimizes this error, and thus fits the data best!

Part 2: Try a bunch of slopes and intercepts!
8.
The way Reggie wants to find a line of best fit is by trial and error. He wants to try a bunch of different slopes (m values) and a bunch of different intercepts (b values) and see which one produces the smallest error value for his dataset.

Using a list comprehension, let’s create a list of possible m values to try. Make the list possible_ms that goes from -10 to 10 inclusive, in increments of 0.1.

9.
Now, let’s make a list of possible_bs to check that would be the values from -20 to 20 inclusive, in steps of 0.1.

10.
We are going to find the smallest error. First, we will make every possible y = m*x + b line by pairing all of the possible ms with all of the possible bs. Then, we will see which y = m*x + b line produces the smallest total error with the set of data stored in datapoints.

First, create the variables that we will be optimizing:

smallest_error — this should start at infinity (float("inf")) so that any error we get at first will be smaller than our value of smallest_error
best_m — we can start this at 0
best_b — we can start this at 0
11.
We want to:

Iterate through each element m in possible_ms
For every m value, take every b value in possible_bs
If the value returned from calculate_all_error() on this m value, this b value, and datapoints is less than our current smallest_error,
Set best_m and best_b to be these values, and set smallest_error to this error.
12.
By the end of these nested loops, the smallest_error should hold the smallest error we have found, and best_m and best_b should be the values that produced that smallest error value.

Print out best_m, best_b and smallest_error after the loops.

Part 3: What does our model predict?
13.
Now we have seen that for this set of observations on the bouncy balls, the line that fits the data best has an m of 0.4 and a b of 1.6:

y = 0.4x + 1.6


This line produced a total error of 5.

Using this m and this b, what does your line predict the bounce height of a ball with a width of 6 to be? In other words, what is the output of get_y() when we call it with:

m = 0.4
b = 1.6
x = 6
14.
Our model predicts that the 6cm ball will bounce 4.0m.

Now, Reggie can use this model to predict the bounce of all kinds of sizes of balls he may choose to include in the ball pit!
"""

# Task 1
# Write your get_y() function here
def get_y(m,b,x):
  y = m*x + b

  return y


# Uncomment each print() statement to check your work. Each of the following should print True
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


# Tasks 2 and 3
# Write your calculate_error() function here
def calculate_error(m, b, point):
  x = point[0]
  y = point[1]

  yvalue = get_y(m,b,x)
  diff = abs(y - yvalue)
  return diff 


# Task 4
# Uncomment each print() statement and check the output against the expected result

# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))

# the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))

# the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))

# the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))


# Task 5
# Write your calculate_all_error() function here
def calculate_all_error(m, b, points):
  error = 0
  for point in points:
    error += calculate_error(m, b, point)

  return error



# Task 6
# Uncomment each print() statement and check the output against the expected result
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]

# every point in this dataset lies upon y=x, so the total error should be zero:
print(calculate_all_error(1, 0, datapoints))

# every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
print(calculate_all_error(1, 1, datapoints))

# every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
print(calculate_all_error(1, -1, datapoints))

# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
print(calculate_all_error(-1, 1, datapoints))


# Tasks 8 and 9
possible_ms = [m / 10 for m in range(-100,101)]
possible_bs = [b / 10 for b in range(-200, 201)]


# Task 10
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0


# Tasks 11 and 12
for m in possible_ms:
  for b in possible_bs:
    error_calc = calculate_all_error(m, b, datapoints)

    if error_calc < smallest_error:
      smallest_error = error_calc
      best_m = m
      best_b = b

print(best_m, best_b, smallest_error)



# Task 13
calc = get_y(m=best_m, b = best_b, x = 6)
print(calc)








