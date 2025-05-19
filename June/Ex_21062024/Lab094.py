# Decorator: function that calls another function and adds functionality/extra behavior without modifying it.
# Decorator: function that takes a function as an argument and returns a new function


def decorator_function(func):
    def wrapper(name):
        print("Starting the function...")
        func(name)
        print("Function finished.")
    
    return wrapper

@decorator_function
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Decorator: function that takes a function as an argument and returns a new function


