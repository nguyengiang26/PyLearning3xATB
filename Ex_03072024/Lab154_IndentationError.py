 
    print("The total number of words in the file is:", len(words)) # IndentationError   

result = 5 + "5" # TypeError: unsupported operand type(s) for +: 'int' and 'str'

int("pramod") # ValueError: invalid literal for int() with base 10: 'pramod'

print(undefine_variable) # NameError: name 'undefine_variable' is not defined

my_list = [1, 2, 3]
print(my_list[3]) # IndexError: list index out of range

my_dict = {"name": "John", "age": 30}
print(my_dict["gender"]) # KeyError: 'gender'

import notFoundModule # ModuleNotFoundError: No module named 'notFoundModule'

import math
print(math.sqrt(-1)) # ValueError: math domain error
math.exp(1000) # OverflowError: math range error


