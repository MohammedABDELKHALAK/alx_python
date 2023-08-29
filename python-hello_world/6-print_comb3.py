
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print("{:02d}".format(tens_digit * 10 + ones_digit), end=", " if tens_digit < 9 or ones_digit < 9 else "\n")
