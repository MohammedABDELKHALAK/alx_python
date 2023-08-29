def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Initialize variables to store the best score and corresponding key
    best_score_value = None
    best_score_key = None

    # Iterate through the dictionary items
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the current best score value
        if best_score_value is None or value > best_score_value:
            best_score_value = value
            best_score_key = key

    # Return the key with the biggest integer value
    return best_score_key