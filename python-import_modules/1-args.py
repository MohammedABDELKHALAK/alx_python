import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name from the count

    # Print the number of arguments
    print(f"{num_args} argument{'s' if num_args != 1 else ''}:")

    # Print each argument with its position (up to the first two arguments)
    for i, arg in enumerate(sys.argv[1:], start=1):

        print(f"{i}: {arg}")

    # Check if no arguments were passed
    if num_args == 0:
        print("0 arguments.")
