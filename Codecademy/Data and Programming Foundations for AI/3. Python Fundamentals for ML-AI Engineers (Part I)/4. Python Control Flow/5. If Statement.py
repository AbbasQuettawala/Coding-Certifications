"""
“Okay okay okay, boolean 
Preview: Docs Loading link description
variables
, boolean expressions, blah blah blah, I thought I was learning how to build control flow into my code!”

You are, I promise you!

Understanding boolean variables and expressions is essential because they are the building blocks of 
Preview: Docs Conditionals take an expression, which is code that evaluates to determine a value, and checks if it is True or False. If it’s True, we can tell our program to do one thing — we can even account for False to do another. As we write more complex programs, conditionals allow us to address multiple scenarios and make our programs more robust. The Python if statement is used to determine the execution of code based on the evaluation of a Boolean expression. - If the if statement expression evaluates to True, then the indented code following the statement is executed. - If the expression evaluates to False then the indented code following the if statement is skipped and the program executes the next line of code which is indented at the same level as the if statement. py test_value = 100
conditional statements
.

Recall the waking-up example from the beginning of this lesson. The decision-making process of “Is it raining? If so, bring an umbrella” is a conditional statement.

Here it is phrased in a different way:

If it is raining, then bring an umbrella.
Can you pick out the boolean expression here?

Right, "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True.

If "it is raining" == True then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:

If [it is raining], then [bring an umbrella]
In Python, it looks very similar:

if is_raining:
  print("bring an umbrella")

Copy to Clipboard

You’ll notice that instead of “then” we have a colon, :. That tells the computer that what’s coming next is what should be executed if the condition is met.

Let’s take a look at another conditional statement:

if 2 == 4 - 2: 
  print("apple")

Copy to Clipboard

Will this code print apple to the terminal?

Yes, because the condition of the if statement, 2 == 4 - 2 is True.

Let’s work through a couple more together.

Instructions
Checkpoint 1 Enabled
1.
In script.py, there is an if statement. I wrote this because my coworker Dave kept using my computer without permission and he is a real doofus. If the user_name is Dave, it tells him to stay off my computer.

Enter a user name in the field for user_name and try running the program.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Oh no! We got a SyntaxError! This happens when we make a small error in the syntax of the conditional statement.

Read through the error message carefully and see if you can find the error. Then, fix it, and run the code again.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Ugh! Dave got around my security and has been logging onto my computer using our coworker Angela’s user name, angela_catlady_87.

Set your user_name to be angela_catlady_87.

Update the program with a second if statement so it checks for Angela’s user name as well and prints

"I know it is you, Dave! Go away!"

Copy to Clipboard

in response. That’ll teach him!
"""

# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")