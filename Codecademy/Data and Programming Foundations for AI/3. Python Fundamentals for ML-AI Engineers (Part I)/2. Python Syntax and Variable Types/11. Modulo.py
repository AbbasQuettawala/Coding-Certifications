"""
ython offers a companion to the division operator called the 
Preview: Docs Loading link description
modulo
 operator. The modulo operator is indicated by % and gives the remainder of a division calculation. If the two numbers are divisible, then the result of the modulo operation will be 0.

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

Copy to Clipboard

Here, we use the modulo operator to find the remainder of division operations. We see that 29 % 5 equals 4, 32 % 3 equals 2, and 44 % 2 equals 0.

Let’s look at another example to get a better idea of how modulo is useful in programming:

print(3 % 3) # Prints 0
print(4 % 3) # Prints 1
print(5 % 3) # Prints 2
print(6 % 3) # Prints 0
print(7 % 3) # Prints 1

Copy to Clipboard

In each of these modulo operations, 3 is the divisor. Since 3 / 3 equals 1 with no remainder, the result of the first modulo operation is 0. Note that as the dividend increases by 1, the remainder also increases by 1, until we reach the next number that is evenly divisible by 3 — this creates a pattern that repeats contiuously as the dividend increases by 1!

Because of this, the modulo operator is useful in programming when we want to perform an action every nth time something occurs. Imagine you own a small café and would like for every 7th customer to receive a survey. If every customer transaction is numbered in the order they occur, you can determine which customers should receive the survey by calculating transaction_number % 7 — if the result is 0, hand out the survey!

"""

first_order_remainder = 269 % 10
print(first_order_remainder)

first_order_coupon = "no"

second_order_remainder = 270 % 10
print(second_order_remainder)

second_order_coupon = "yes"