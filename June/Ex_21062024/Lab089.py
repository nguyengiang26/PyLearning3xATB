# SET: Collect of unique, unorederd items
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.union(set2)  # Union of two sets
print(set3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

set4 = set1.intersection(set2)  # Intersection of two sets 
print(set4) # Output: {4, 5}

set5 = set1.difference(set2)  # Difference of two sets
print(set5)  # Output: {1, 2, 3}


