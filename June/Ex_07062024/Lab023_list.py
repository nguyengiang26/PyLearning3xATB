# List - Shopping List
# milk, bread, eggs, cheese
"""
1. Add item
2. Remove item
3. Update item
4. View item
5. Exit
"""

shopping_list = ["milk","bread","eggs","cheese"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])

shopping_list.append("curd") # add item in the end
print(shopping_list)
shopping_list.insert(3,"jam") #add item in the middle
print(shopping_list)
shopping_list.remove("bread") #remove item
print(shopping_list)
shopping_list.pop(0) #remove item in the middle
print(shopping_list)
shopping_list.reverse() #reverse the list
print(shopping_list)