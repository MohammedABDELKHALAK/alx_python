raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg
message = "C is fun"

try:
    if message == "C is fun":
       raise_exception_msg(message)

    elif message == "Python is cool":
         raise_exception_msg(message)

except NameError as ne:
    
    print(ne)