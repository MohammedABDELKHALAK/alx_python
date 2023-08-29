def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row
        for i, element in enumerate(row):
            # Use str.format() to print each element as an integer
            print("{:d}".format(element), end="")
            # If it's not the last element in the row, print a space to separate elements horizontally
            if i != len(row) - 1:
                print(" ", end="")
        # After each row, print a new line to separate rows vertically
        print()