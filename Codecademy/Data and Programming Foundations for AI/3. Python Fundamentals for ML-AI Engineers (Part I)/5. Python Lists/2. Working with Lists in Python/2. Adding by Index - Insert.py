"""
The Python list method .insert() allows us to add an element to a specific index in a list.

The 
Preview: Docs Loading link description
.insert()
 method takes in two inputs:

The index you want to insert into.
The element you want to insert at the specified index.
The .insert() method will handle shifting over elements and can be used with negative indices.

To see it in action let’s imagine we have a list representing a line at a store:

store_line = ["Karla", "Maxium", "Martim", "Isabella"]

Copy to Clipboard

"Maxium" saved a spot for his friend "Vikor" and we need to adjust the list to add him into the line right behind "Maxium".

For this example, we can assume that "Karla" is the front of the line and the rest of the elements are behind her.

Here is how we would use the .insert() method to insert "Vikor" :

store_line.insert(2, "Vikor")
print(store_line) 

Copy to Clipboard

Would output:

 ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']

Copy to Clipboard

Some important things to note:

The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.

When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift.

Let’s practice using .insert()!

Instructions
Checkpoint 1 Enabled
1.
We are helping out a popular grocery store called Jiho’s Produce.

Every week the store has to choose the order in which it displays some of its popular items on sale in the front window to attract customers.

Jiho, the store owner, likes to store the items for the display in a list.

Check out the current display list in our code editor. Click Run to print out the list.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Jiho found out some great news! "Pineapple" is back in stock.

Jiho would like to put "Pineapple" in the front of the list so it is the first item customers see in the display window.

Use .insert() to add "Pineapple" to the front of the list.

Print the resulting list to see the change.

Note: For this list, the front will be the element at index 0
"""

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")