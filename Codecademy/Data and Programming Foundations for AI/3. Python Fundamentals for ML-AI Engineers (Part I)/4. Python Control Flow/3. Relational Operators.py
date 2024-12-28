"""
Now that we understand Boolean expressions, let’s learn how to create them. In Python, we create Boolean expressions using relational and logical operators.

Relational operators compare two values and return True or False based on the operands. For this reason, you will sometimes hear them called 
Preview: Docs Loading link description
comparison operators
.
Logical operators are used to combine multiple Boolean expressions.
The two relational operators we’ll cover first are equals to and not equals to.

The equals to operator (==) returns True if both its operands are the same. Otherwise, it returns False. For example, the Boolean expression a == b will return True if the values a and b are the same. Otherwise, it will return False.

The not equals to operator (!=) is the negation of the equals to operator. The Boolean expression a != b will return True if the values a and b are different. Otherwise, it will return False.

We can create Boolean expressions by comparing two values using these operators as shown below:

1 == 1     # Evaluates to True as the operands are the same 

1 != 1     # Evaluates to False as the operands are the same 

2 != 4     # Evaluates to True as the operands are different 

3 == 5     # Evaluates to False as the operands are different
 
'7' == 7   # Evaluates to False as the operands are different types 

Copy to Clipboard

Instructions
Checkpoint 1 Enabled
1.
Determine if the following Boolean expression is True or False. Assign your answer as True or False in the variable first_expression.

2 * 2 == 2 + 2

Copy to Clipboard

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Next, consider the following expression:

3 + 3 != 3 * 3 

Copy to Clipboard

If the above Boolean expression is True, initialize a variable second_expression to True. Otherwise, initialize it to False.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Now, consider this expression:

3 * 3 == '9'

Copy to Clipboard

If the above Boolean expression is True, initialize a variable third_expression to True. Otherwise, initialize it to False.
"""

first_expression = True
second_expression = True
third_expression = False