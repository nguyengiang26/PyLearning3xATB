# Filter in Python
# Filter is a built-in function in Python that allows you to filter elements from an iterable (like a list, tuple, or set)
# based on a function that returns True or False.

# The filter function takes two arguments: a function and an iterable.
# It applies the function to each element of the iterable and returns a new iterable containing only the elements for which the function returned True.
# The filter function is often used in conjunction with lambda functions to create concise and readable code.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter even numbers from the list

def is_even(number):
    return number % 2 == 0

new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))  # Output: [2, 4, 6, 8, 10]

