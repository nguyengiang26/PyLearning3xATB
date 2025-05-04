# args
def print_args(*args): # Variable-length arguments
    for i in args:
        print("Hello", i, end = "\n")

print_args("Giang", "John", "Mary")  # Calls with multiple arguments
