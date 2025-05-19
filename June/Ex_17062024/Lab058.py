def Hello(): # No return value & no parameters
    print("Hello")

def say_hello_default(name="Giang"): # Default parameter
    print(f"Hello {name}")

say_hello_default()  # Calls with default name
say_hello_default("John")  # Calls with provided name


