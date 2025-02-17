"""
Frida Kahlo Retrospective Off-Platform Project
Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building.

There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

Project Goals
Congratulations! You’ve been hired to work on a retrospective of Frida Kahlo’s work at a major museum in Mexico.

Your job is to put together the audio tour, but in order to do that, you need to create a list of each painting featured in the exhibit, the date it was painted, and its spot on the tour.

Use your knowledge of Python lists to create a master list of each painting, its date, and its audio tour ID.

Setup
We encourage you to complete this project on your own computer using Jupyter notebooks. To do so, continue following these instructions to get going.

If you’d prefer, you may also use the Codecademy learning environment to do this assignment. Get started by skipping the rest of these setup instructions and instead clicking Start. Then, complete the tasks in the code editor.

To work on this project on your own machine, you will need to use some external tools: the Command Line and Jupyter Notebooks. If you are not familiar with these topics, check out our course on Getting Started Off-Platform for Data Science for help getting set up.

Once you’re ready to begin, click Download to get the zip file containing all of the project files. Extract the files and open frida_kahlo_retrospective.ipynb to start working! If you get stuck, you can take a look at frida_kahlo_retrospective_solution.ipynb for the correct answers.

Note: Be sure to check off the Tasks here on Codecademy even if you are working on this project off-platform. The project will not be considered completed and counted toward your Course or Path Progress until all tasks have been checked off.

Download
Tasks
0/8 complete
Mark the tasks as complete by checking them off
1.
First, create a list called paintings and add the following titles to it:

'The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys'

2.
Next, create a second list called dates and give it the following values:

1939, 1933, 1946, 1940

3.
It doesn’t do much good to have the paintings without their dates, and vice versa. Zip together the two lists so that each painting is paired with its date and resave it to the paintings variable. Make sure to convert the zipped object into a list using the list() function. Print the results to the terminal to check your work.

4.
There were some last minute additions to the show that we need to add to our list. Append the following paintings to our paintings list then re-print to check they were added correctly:

'The Broken Column', 1944
'The Wounded Deer', 1946
'Me and My Doll', 1937
5.
Since each of these paintings is going to be in the audio tour, they each need a unique identification number. But before we assign them a number, we first need to check how many paintings there are in total.

Find the length of the paintings list.

6.
Use the range method to generate a list of identification numbers that starts at 1 and is equal in length to our list of items. Save the list to the variable audio_tour_number and check your work by printing the list.

7.
We’re finally ready to create our master list. Zip the audio_tour_number list to the paintings list and save it as master_list.

8.
Print the master_list to the terminal.
"""

paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]
new = list(zip(paintings,dates))
print(new)
new.append(("The Broken Column", 1944))
new.append(("The Wounded Deer", 1946))
new.append(("Me and My Doll", 1937))
print(new)
lenght = len(new)
audio_tour_number = range(lenght)
master_list = list(zip(audio_tour_number,new))
print(master_list)