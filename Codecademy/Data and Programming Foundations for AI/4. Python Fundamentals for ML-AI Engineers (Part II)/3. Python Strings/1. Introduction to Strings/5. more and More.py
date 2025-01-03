"""
.
Copeland’s Corporate Company also wants to update how they generate temporary passwords for new employees.

Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates the last three letters of each and returns them as a string.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Test your function on the provided first_name and last_name and save it to the variable temp_password.
"""

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)