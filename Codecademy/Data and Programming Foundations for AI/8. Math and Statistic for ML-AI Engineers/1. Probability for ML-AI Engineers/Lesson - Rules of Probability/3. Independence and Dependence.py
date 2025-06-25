'''
Imagine that we flip a fair coin 5 times and get 5 heads in a row. Does this affect the probability of getting heads on the next flip? Even though we may feel like it’s time to see “tails”, it is impossible for a past coin flip to impact a future one. The fact that previous coin flips do not affect future ones is called independence. Two events are independent if the occurrence of one event does not affect the probability of the other.

Are there cases where previous events DO affect the outcome of the next event? Suppose we have a bag of five marbles: two marbles are blue and three marbles are red. If we take one marble out of the bag, what is the probability that the second marble we take out is blue?

A diagram of the possible outcomes of pulling two marbles out of a bag when pulling them out without replacement.

This describes two events that are dependent. The probability of grabbing a blue marble in the second event depends on whether we take out a red or a blue marble in the first event.

What if we had put back the first marble? Is the probability that we pick a blue marble second independent or dependent on what we pick out first? In this case, the events would be independent.

A diagram of the possible outcomes of pulling two marbles out of a bag when pulling them out with replacement.

Why do we care if events are independent or dependent? Knowing this helps us quantify the probability of events that depend on preexisting knowledge. This helps researchers understand and predict complex processes such as:

Effectiveness of vaccines
The weather on a particular day
Betting odds for professional sports games
We will explore applications of this further in the lesson!

Instructions
Checkpoint 1 Enabled
1.
In quiz.py we have the following variables: events_1, events_2, and events_3. Given the two events outlined in these exercises, fill in the variables as either "dependent" or "independent".

We pick out two cards from a standard deck of 52 cards without replacement. Event A is that we pick an Ace on the first draw. Event B is that we pick an Ace on the second draw. Are events A and B independent?

Fill in your answer in the "insert answer here" section of the events_1 variable. After filling out your answer in quiz.py, hit run.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Suppose we roll a six-sided die two times. Event A is that we roll a 3 on the first roll. Event B is that we roll a 3 on the second roll. Are events A and B independent?

Fill in your answer in the "insert answer here" section of the events_2 variable. After filling out your answer in quiz.py, hit run.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Suppose we flip a coin ten times. Event A is that we flip all heads on the first five flips. Event B is that we flip all heads on the second five flips. Are events A and B independent?

Fill in your answer in the "insert answer here" section of the events_3 variable. After filling out your answer in quiz.py, hit run.
'''

events_1 = "dependent"
events_2 = "independent"
events_3 = "independent"