"""
We’ve iterated through lists that have a discrete beginning and end. However, let’s consider this example:

my_favorite_numbers = [4, 8, 15, 16, 42]

for number in my_favorite_numbers:
  my_favorite_numbers.append(1)

Copy to Clipboard

Take some time to ponder what happens with this code.

Click to see what would happen!

A loop that never terminates is called an infinite loop. These are very dangerous for our code because they will make our program run forever and thus consume all of your computer’s resources.

A program that hits an infinite loop often becomes completely unusable. The best course of action is to avoid writing an infinite loop.

Note: If you accidentally stumble into an infinite loop while developing on your own machine, you can end the loop by using control + c to terminate the program. If you’re writing code in our online editor, you’ll need to refresh the page to get out of an infinite loop.

Let’s fix an infinite loop to see it in action.

Instructions
Suppose we have two lists of students, students_period_A and students_period_B. We want to combine all students into students_period_B.

In your code editor, we have provided you a loop. Go ahead and uncomment line 5 and before you run the code ponder why this code would cause an infinite loop.

When you are ready, run this code. What do you notice happens? Over the run button, notice the loading circle is continuing without anything happening.

This is an infinite loop! To end this program we must refresh the page. (Note: The reason this loop is infinite is that we’re adding each student in students_period_A to students_period_A which would create a never-ending list of all the student names.)
"""

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)