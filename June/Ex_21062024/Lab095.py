'''
DICt
Key and value are separated by a colon (:)
key should be unique
unordered collection of items

'''
my_dict = {
    "name": "Ali",
    "age": 25,
    "city": "Cairo"
}

print(my_dict["name"]) # Output: Ali
print(my_dict["age"]) # Output: 25

print(my_dict.get("name")) # Output: Ali
print(my_dict.values()) # Output: dict_values(['Ali', 25, 'Cairo'])
print(my_dict.keys()) # Output: dict_keys(['name', 'age', 'city'])


print(my_dict.__len__()) # Output: 3
print(len(my_dict)) # Output: 3


import Ex_24062024.Lab096 as Lab096
print(Lab096.SetName()) # Output: Lab096
