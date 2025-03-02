# For Loop Functions
'''
i = 1
while i <= 10:
    print(i,end = " ")
    i += 1
print("")

for i in range(1,10):
    print(i)

bag = ("red","green","blue")
for ball in bag: # ball is a variable
    print(ball)
'''

# Enumerate 
'''
name = "Darshan"
for index, letter in enumerate(name):
    print(letter*(index+1))

l = [9,8,7,6,5,4,3,2,1]

for index, num in enumerate(l):
    print(f"{num} is in {index} index")
'''
# Else in for loop
'''
n = [1,2,3,4,5,6]
for num in n:
    print(num)
    if num == 4:
        break
else:
    print("All Printed")

d = {"name":"Darshan","age":21,"income":300000}
# print(d.items()) # converts Dic to tuples , Try this once if u want
for key, Value in d.items(): # d.items() converts dic to tuples and list
    print(key,"",Value)
'''
'''
# multiplication 2 Table
for n in range(1,11):
    print(f"2x{n}={n*2}")
    # print(f"6x{n}={n*6}") For 6 Table
'''
# Nested Loop (Tables from 2 to 10)
for i in range(21,28):
    for j in range(1,11):
      #  print(f"2x{j}={i*2}")
      print(f"{i}x{j}={i*j}")