# Tuples and Sets
# Tuple 
''' gender = ("male","female") # Tuple ()
print(type(gender)) 
print(len(gender)) # We can't add and change elements in tuples
print(gender.index("male"))
#print(gender(0)) # tuple object is not calable
'''
 
# Sets 
'''
s = {1,5,4,76,1,4,34}
my_set = {"element1", "element2", "element3"}
print(s) # sets are unordered 
s2 = set((1,2,3,3,1))
print(type(s2)) '''

# Union , intersection, difference
'''s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1 | s2) # Union
print(s1 & s2) # Intersection (which are in both)
print(s1 - s2) # Difference '''

'''
s = {1,2,3,4,5,6}
s.add(10)
s.remove(1) #  Gives error if element is not there 
s.discard(3) # it will remove if 10 is there orelese just leaves without giving error
s.pop() # Removes any one of the element 
print(s)'''

# set = {}
# tuple = ()
# list = []