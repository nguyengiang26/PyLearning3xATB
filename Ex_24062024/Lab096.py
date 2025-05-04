# Python  - Vast - Not all the functions are required to build you
# Automation Tester - API and Web Automation

my_dict = {
    'b': 2,
    'a': 1,
    'c': 3
}

# To find a key in a dictionary, you can use the `in` operator
# This will return True if the key is present in the dictionary, and False otherwise.
for k in my_dict: # Iterate through the keys in the dictionary
    if k == 'b':
        print('Key found')

for k in my_dict.keys(): # Iterate through the keys in the dictionary
    if k == 'b':
        print('Key found')

for v in my_dict.values(): # Iterate through the values in the dictionary
    if v == 1:
        print('Value found')

for k, v in my_dict.items(): # Iterate through the key-value pairs in the dictionary
    print(k, v) # Print the key and value

print('Key b is found in the dictionary') if 'b' in my_dict else print('Key not found')

