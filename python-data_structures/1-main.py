#!/usr/bin/python3
print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix1 = [[1, 2], [4, 5]]

matrix2 = [[1, 2], [4, 5], [7, 8]]

matrix3 = [[1]]

matrix4 = [[1], [2], [3], [4]]

print_matrix_integer(matrix)
print("--")

print_matrix_integer(matrix1)
print("--")

print_matrix_integer(matrix2)
print("--")

print_matrix_integer(matrix3)
print("--")

print_matrix_integer(matrix4)
print("--")
print_matrix_integer()
