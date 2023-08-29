def safe_print_division(a, b):

    try:
        result = a / b

    except ZeroDivisionError:
        # print("Cannot divide by zero.")
        result = None      
        return result
    
    finally:
         print("Inside result: {}".format(result))
         return result