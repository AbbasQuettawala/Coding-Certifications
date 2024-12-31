"""
Sometimes you want to simulate a lot of different scenarios. It would be very expensive to run thousands of tests, but it’s very cheap to generate thousands of results.

In this exercise, we are going to simulate binomial data. Binomial distributions are very useful for modeling different types of data, from drug treatment effectiveness to stock price trends.

Binomial events always have 2 possible outcomes, which we refer to as success and failure. The probability of a successful outcome is represented by the parameter p. For example, for the event of a coin toss using a fair coin, p would be 0.5.

There are lots of ways to do this. We could flip a coin a bunch of times and write down the results or we could use the random.binomial() method from the numpy library in Python.

To use the random.binomial() method, we have to tell it how many trials we want to simulate (n) and the probability of ‘success’ in a single trial (p), and how many experiments to run.

In the example below, there was 1 flip per trial (n), the probability (p) of getting ‘success’ was .5 (the coin is fair), and we conducted the experiment 2,000 times (size).


print(numpy.random.binomial(n = 1, p = 0.5, size=2000))

Copy to Clipboard

The output from our simulation is a list of 0’s and 1’s. This is the number of successes in each experiment. In this case, since we are simulating a single trial, 1 would mean the outcome of the trial was a success and 0 would mean the outcome was a failure.

If we wanted to do 10 flips per experiment, the result would be a list of numbers from 0 to 10 representing the number of successes in each experiment.

print(numpy.random.binomial(n=10, p=0.5, size=2000))

Copy to Clipboard

Binomial distributions are really cool – and you will definitely see them again in your Data Science journey. Let’s practice creating some now.

Instructions
Checkpoint 1 Enabled
1.
Start by importing the numpy library.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Call the random.binomial() method to simulate

a single (1) coin toss
using a biased coin that has a 0.8 probability of landing on heads. We’ll call heads successful.
conducted 500 times.
Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Now let’s increase the number of trials per experiment.

Call the random.binomial() method to simulate

100 tosses
using a biased coin that has a 0.8 probability of landing on heads. We’ll call heads successful.
conducted 500 times.
"""

import numpy
print(numpy.random.binomial(n = 1, p = 0.8, size = 500))
print(numpy.random.binomial(n = 100, p = 0.8, size = 500))