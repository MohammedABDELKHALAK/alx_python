def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C'
        if char != 'c' and char != 'C':
            # If not 'c' or 'C', add the character to the result string
            result += char
            
    # Return the final result string
    return result