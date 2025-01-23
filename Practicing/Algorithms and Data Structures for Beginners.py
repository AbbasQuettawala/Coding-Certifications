# Algorithms and Data Structures for Beginners

# Time Complexity:
# O(1) - Constant Time - The runtime does not depend on the input size. Always takes the same amount of time.
# O(log n) - Logarithmic Time - The runtime grows slowly as the input size increases (e.g., binary search).
# O(n) - Linear Time - The runtime grows proportionally with the input size.
# O(n log n) - Linearithmic Time - Common in efficient sorting algorithms (e.g., Merge Sort, Quick Sort).
# O(n^2) - Quadratic Time - Runtime grows quadratically with the input size (e.g., nested loops).
# O(2^n) - Exponential Time - Runtime doubles with each additional input element (e.g., brute-force solutions to combinatorics).

# Static Arrays:
# Static arrays are a type of data structure where the size of the array is fixed at the time of creation and cannot be changed during its lifetime, Size of array remains the same, but the values can be changed
arr = [0] * 5 
print(arr)

# Dynamic Arrays:
# Dynamic arrays are a type of data structure where the size of the array can be changed during runtime. Size and values both can be changed

# Stacks:
# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means the last element added to the stack is the first one to be removed.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
    

    # Singly Linked Lists:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A class to represent the singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the list as empty (head is None)

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    def delete_by_value(self, value):
        """Delete the first occurrence of a node with the given value."""
        if not self.head:  # If the list is empty
            print("List is empty!")
            return

        # If the node to delete is the head
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        # If the value is not found
        if not current.next:
            print("Value not found in the list!")
            return

        # Skip the node to delete it
        current.next = current.next.next

    def traverse(self):
        """Traverse the list and print all elements."""
        if not self.head:
            print("List is empty!")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Doubly Linked Lists
# A doubly linked list is a data structure where each node contains three parts:

# Data: The value stored in the node.
# Next Pointer: A reference to the next node in the sequence.
# Previous Pointer: A reference to the previous node in the sequence.

class Node:
    """A class to represent a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    """A class to represent the doubly linked list."""
    def __init__(self):
        self.head = None  # Initialize the list as empty (head is None)

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning."""
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end."""
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete_by_value(self, value):
        """Delete the first occurrence of a node with the given value."""
        if self.head is None:  # If the list is empty
            print("List is empty!")
            return

        # If the node to delete is the head
        if self.head.data == value:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return

        current = self.head
        while current and current.data != value:
            current = current.next

        if current is None:  # Value not found
            print("Value not found in the list!")
            return

        # Update pointers to remove the node
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def traverse_forward(self):
        """Traverse the list in forward direction."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Traverse the list in backward direction."""
        current = self.head
        if current is None:
            print("List is empty!")
            return

        # Go to the last node
        while current.next:
            current = current.next

        # Traverse backward
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")


# Insertion sort:
# Will sort an array to make an item fit, probably in ascending or descending order

# Merged Sort:
# Merge Sort is a divide and conquer sorting algorithm that divides the array into smaller subarrays, sorts them, and then merges them back together in sorted order.


