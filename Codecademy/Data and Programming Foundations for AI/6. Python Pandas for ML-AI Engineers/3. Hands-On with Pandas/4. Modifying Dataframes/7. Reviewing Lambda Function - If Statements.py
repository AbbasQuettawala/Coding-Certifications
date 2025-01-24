"""
We can make our lambdas more complex by using a modified form of an if statement.

Suppose we want to pay workers time-and-a-half for overtime (any work above 40 hours per week). The following function will convert the number of hours into time-and-a-half hours using an if statement:

def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x


Below is a lambda function that does the same thing:

myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x


In general, the syntax for an if function in a lambda function is:

lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]


Instructions
Checkpoint 1 Enabled
1.
You are managing the webpage of a somewhat violent video game and you want to check that each user’s age is 13 or greater when they visit the site.

Write a lambda function that takes an inputted age and either returns Welcome to BattleCity! if the user is 13 or older or You must be 13 or older if they are younger than 13. Your lambda function should be called mylambda.
"""

import codecademylib3

mylambda = lambda x: 'Welcome to BattleCity!' \
	if x >= 13 \
  else 'You must be 13 or older'