# Dictionaries Operations
details = {
    "name": "Darshan", # Key : value
    "age": "21",
    "college": "tjohn"
}
# print(details)
#print(type(details))
'''
print(details["name"]) # you should use [] only for calling
# print(details("name"))
print(details.get("gender")) # Gives none without giving error
print(details.get("gender", "Not found")) # Prints not Found

details["gender"] = "Male" # Adding gender
print(details["gender"])
details["name"] = "Darshan M S" # Updating elements (used to chane name)
print(details)
details.pop("age") # used to pop certain thing (we can assign this to a varible )
del details["college"] # another method for removing (we can't assign to variable)
print(details)
print(details.keys()) # Gives only keys 
print(details.values()) # Gives only values
print(details.items()) # Give keys and values inside a tuple
'''

# update
'''
marks = { 
    "maths" : 99,
    "science" : 90,
    "social" : 95 
}
details.update(marks) # updated details with marks also
print(details) 
'''
item1 = {
    "name" : "milk",
    "weight" : 1,
    "price" : 50
}
item2 = {
    "name" : "sugar",
    "weight" : 2,
    "price" : 90
}
item3 = {
    "nmae" : "coffe powder",
    "weight" : 0.25,
    "price" : 150
}
items = [item1,item2,item3]
# print(items)

# Adding values (Total weight of all items)
print(f"Total weight : {item1["weight"]+item2["weight"]+item3["weight"]} kg")

