def multiple_returns(sentence):
        # Get the length of the sentence
    length = len(sentence)

    # Get the first character of the sentence
    first_char = None if length == 0 else sentence[0]

    # Return the tuple with the length and first character
    return length, first_char
