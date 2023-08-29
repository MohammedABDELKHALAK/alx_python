#!/usr/bin/python3

# Import the Square class from 4-square module
Square = __import__('4-square').Square

# Create a square instance with size 3
my_square = Square(3)

# Print my_square using my_print method
my_square.my_print()
# Output:
# ###
# ###
# ###

print("--")

# Set the size of my_square to 10
my_square.size = 10

# Print my_square using my_print method
my_square.my_print()
# Output:
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########

print("--")

# Set the size of my_square to 0
my_square.size = 0

# Print my_square using my_print method
my_square.my_print()
# Output: 
#

print("--")

