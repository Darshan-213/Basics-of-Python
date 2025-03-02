# List
'''item1 = "Milk"
item2 = "Sugar"
item3 = "Pepsi"
print(item1, item2, item3) '''

# Indexing and Modifing list
items = ["milk", "sugar", "pepsi", "apple", 4, 987, True, (1,2,3)]
print(items)
print(items[1:])
print(items[-1])
items.pop() # Last item is removed
items.pop(0) # Removed first element
print(items)
items.append("Buscuits")
items.remove("pepsi")
items.insert(2, "7 up") # Inserting value by giving index number
# items.clear()
items[3] = "Coffe"

# Sort and Reverse 
item3 = [3,4,9,32,1,54]
item3.sort()
print(item3)
s_items = sorted(item3)
rev = s_items.reverse() # Try this 
print(rev)