
"""
Computers absolutely excel at performing calculations. The “compute” in their name comes from their historical association with providing answers to mathematical questions. Python performs the 
Preview: Docs Loading link description
arithmetic operations
 of addition, subtraction, multiplication, and division with +, -, *, and /.

# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)

# Prints "2.0"
print(10 / 5)

Copy to Clipboard

Notice that when we perform division, the result has a decimal place. This is because Python converts all ints to floats before performing division. In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division would always round down to the nearest integer.

Division can throw its own special error: ZeroDivisionError. Python will raise this error when attempting to divide by 0.

Mathematical operations in Python follow the standard mathematical 
Preview: Docs Operators are used to perform various operations on variables and values.
order of operations
"""

print(25 * 68 + 13 / 28)