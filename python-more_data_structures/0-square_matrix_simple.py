def square_matrix_simple(matrix=[]):
    # Create an empty list to store the squared values
    squared_matrix = []

    # Iterate through each row in the matrix
    for row in matrix:
        # Create an empty list to store the squared values of the current row
        squared_row = []
        # Iterate through each element in the row and compute its square
        for element in row:
            squared_row.append(element ** 2)
        # Add the squared row to the squared matrix
        squared_matrix.append(squared_row)

    # Return the squared matrix
    return squared_matrix