'''
Probability, Set Theory, and the Law of Large Numbers
Learn about what probability is and the language we use to represent it!

Probability
Probability is a branch of mathematics that allows us to quantify uncertainty. In our daily lives, we often use probability to make decisions, even without thinking about it!

For example, many weather reports give a percent chance that it will rain. If we hear that there is an 80 percent chance of rain, we probably are not going to make many plans outside. However, if there is only a 5 percent chance of rain, we may feel comfortable planning a picnic.

In this article, we are going to build a foundation for understanding probability. To do this, we are going to explore a field of mathematics called set theory.

Set Theory
Set theory is a branch of mathematics based around the concept of sets. In simple terms, a set is a collection of things. For example, we can use a set to represent items in a backpack. We might have:

{
B
o
o
k
,
P
a
p
e
r
,
F
o
l
d
e
r
,
H
a
t
,
P
e
n
,
S
n
a
c
k
}
{Book,Paper,Folder,Hat,Pen,Snack}
Notationally, mathematicians often represent sets with curly braces. Sets also follow two key rules:

Each element in a set is distinct.
The elements in a set are in no particular order.
Therefore, we can say:

{
1
,
2
,
3
,
4
,
5
}
=
{
5
,
3
,
2
,
4
,
1
}
{1,2,3,4,5}={5,3,2,4,1}
When defining a set, we often use a capital letter. For example:

A
=
{
1
,
2
,
3
,
4
,
5
}
A={1,2,3,4,5}
Sets can also contain subsets. Set A is a subset of set B if all the elements in A exist within B. For example:

A
=
{
1
,
2
,
3
}
B
=
{
1
,
2
,
3
,
4
,
5
}
A={1,2,3}
B={1,2,3,4,5}
​
 
Here, set A is a subset of B because all elements of A are contained within B.

Experiments and Sample Spaces
In probability, an experiment is something that produces observation(s) with some level of uncertainty. A sample point is a single possible outcome of an experiment. Finally, a sample space is the set of all possible sample points for an experiment.

For example, suppose that we run an experiment where we flip a coin twice and record whether each flip results in heads or tails. There are four sample points in this experiment: two heads (HH), tails and then heads (TH), heads and then tails (HT), or two tails (TT). We can write the full sample space for this experiment as follows:

S
=
{
H
H
,
T
T
,
H
T
,
T
H
}
S={HH,TT,HT,TH}
Suppose we are interested in the probability of one specific outcome: HH. A specific outcome (or set of outcomes) is known as an event and is a subset of the sample space. Three events we might look at in this sample space are:

Getting Two Heads
A
=
{
H
H
}
Getting Two Tails
B
=
{
T
T
}
Getting Both a Heads and Tails
C
=
{
H
T
,
T
H
}
Getting Two Heads
A={HH}
Getting Two Tails
B={TT}
Getting Both a Heads and Tails
C={HT,TH}
​
 
The frequentist definition of probability is as follows: If we run an experiment an infinite amount of times, the probability of each event is the proportion of times it occurs. Unfortunately, we don’t have the ability to flip two coins an infinite amount of times — but we can estimate probabilities by choosing some other large number, such as 1000. Let’s give it a try!

Okay, we have flipped two coins 1000 times. Wasn’t that FUN? Here are each of the outcomes and the number of times we observed each one:

{HH}: 252
{TT}: 247
{HT}: 256
{TH}: 245
To calculate the estimated probability of any one outcome, we use the following formula:

P
(
E
v
e
n
t
)
=
Number of Times Event Occurred
Total Number of Trials
P(Event)= 
Total Number of Trials
Number of Times Event Occurred
​
 
In this scenario, a trial is a single run of our experiment (two coin flips). So, the probability of two heads on two coin flips is approximately:

P
(
H
H
)
=
2
5
2
1
0
0
0
=
.
2
5
2
P(HH)= 
1000
252
​
 =.252
Based on these 1000 trials, we would estimate there is a 25.2 percent chance of getting two heads on two coin flips. This is great! However, if we do this same procedure over and over again, we may get slightly different results. For example, if we repeat the experiment another 1000 times, we might get two heads only 24.2 percent of the time.

If we want to feel confident that we are close to the true probability of a particular event, we can leverage the law of large numbers.

Law of Large Numbers
We can’t repeat our random experiment an infinite amount of times (as much FUN as that would be!). However, we can still flip both coins a large number of times. As we flip both coins more and more, the observed proportion of times each event occurs will converge to its true probability. This is called the law of large numbers.

Let’s observe the law of large numbers in real-time. We will use Python to simulate flipping both coins as many times as we want and watch the proportion of two heads converge to its true probability.

Let’s walk through each part of the code below one step at a time. You do not need to worry about every line of code, but understanding the overall objective will help you build your understanding of probability.

Coding question
Questions
In the code editor below, we have written out a function called coin_flip_experiment() that simulates flipping two fair coins. Using a for loop we run coin_flip_experiment() a specific number of times. As this loop iterates, we track how often both coins come up as heads. Finally, using matplotlib, we plot the proportion of experiments resulting in two heads after each trial.

The number of times coin_flip_experiment() runs is determined by the num_trials variable on line 21. Currently, this variable is set to 5. Run the program a few times. On the resulting plot, the orange horizontal line is the true probability of observing two heads (0.25). The blue line is the proportion of heads we see throughout our trials. What do you notice about the blue line after each run?

You should see that the proportion of two heads after five trials is inconsistent. In some experiments, we may see zero observations of two heads, while in others, we may see almost all five observations are two heads. To simulate the law of large numbers, we need to do more trials. Set the num_trials variable to different values, such as these below:

100
1000
100000
Take note of what you observe. Where does the blue line on the graph converge to after many trials?
'''

import matplotlib.pyplot as plt
import numpy as np
import codecademylib3

def coin_flip_experiment():
  # defining our two coins as lists
  coin1 = ['Heads', 'Tails']
  coin2 = ['Heads', 'Tails']
 
  # "flipping" both coins randomly
  coin1_result = np.random.choice(coin1)
  coin2_result = np.random.choice(coin2)
 
  # checking if both flips are heads
  if coin1_result == 'Heads' and coin2_result == 'Heads':
    return 1
  else:
    return 0
 
# how many times we run the experiment
num_trials = 5
prop = []
flips = []
# keep track of the number of times heads pops up twice
two_heads_counter = 0
 
# perform the experiment five times
for flip in range(num_trials):
  # if both coins are heads add 1 to the counter
  two_heads_counter += coin_flip_experiment()
  # keep track of the proportion of two heads at each flip 
  prop.append(two_heads_counter/(flip+1))
  # keep a list for number of flips
  flips.append(flip+1)
 
# plot all flips and proportion of two heads
plt.plot(flips, prop, label='Experimental Probability')
plt.xlabel('Number of Flips')
plt.ylabel('Proportion of Two Heads')

plt.hlines(0.25, 0, num_trials, colors='orange', label='True Probability')
plt.legend()


 
plt.show()

'''
Play around with the num_trials variable!
After setting num_trials to large numbers, we see that the proportion of trials resulting in two heads converges to 0.25. The horizontal line at y=0.25 is completely covered after about one hundred thousand flips. By simulating a huge number of flips in Python, we have shown that the true probability of seeing two heads on two separate coin flips is equal to 0.25.

Review
We have covered:

An introduction to probability
An introduction to set theory
Sample spaces and events
The law of large numbers
This completes our brief introduction to what probability is and how we can represent it. Now, it’s time to dive into ways we can calculate probability and expand on our knowledge.
'''