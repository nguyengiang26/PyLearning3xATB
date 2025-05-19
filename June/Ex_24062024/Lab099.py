numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def double(number):
    return number * 2

doubled_number = map(double, numbers)
print(list(doubled_number))  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]