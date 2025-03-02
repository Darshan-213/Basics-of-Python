# Home work Questions 

# print("Hello I'm Darshan")
'''a, b = 21,32
print(a+b)
print(a-b)
print(a/b)
print(a*b)

# swaping 
a , b = 10,20
b,a=a,b
print(a,b)

a = a+b
b = a-b
a = a-b

name = input("Enter you namr:")
age = int(input("Enter the age :"))
print(f"Hello {name},you are {age}years old")

s = input("Enter the sentence :")
print(s.upper())
print(s.lower())
s = s.replace(" ","_")
print(s)
print(s.strip()) # to delete the spaces in the first and last

s = input("Enter the string:")
print(len(s.replace(" ","")))
print("hello \n hi \t 213")

a = int(input("Enter the first no:"))
b = int(input("Enter the second no:"))
print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>5))

age = int(input("Enter the age:"))
if age>=18:
    print("Your Audult")
else:
    print("Your Child")

s = input("Enter the string:")
print("a" in s)
print("python" not in s)
# bitwise operators
a=12
b=21
print(a|b)
print(a&b)
print(a^b)
print(a<<2)
print(b>>1)
'''
# List operation
'''
l = [1,2,3,12,32,4,5,43]
l.append(6)
l.insert(2,7)
print(l)
# del l(2)
l.remove(l[2])
print(l)
l.sort()
print(l)
l.sort(reverse=True) # one more type print(l[::-1])
print(l) '''

# Tuples and Sets
'''
t = ("hello",21,"hi",87,"da")
#t[1]=="darshan"
print(t[1:3])
t1 = (1,2,3,4,5)
ad = t + t1 # Concatinating tuples
print(ad) 

my = {"apple","mango"}
fri = {"apple","cheery","grapes"}
print(my | fri) # union
print(my & fri) # Intersection
print(my - fri) # Difference
print(my ^ fri) # Symmetric difference
my.add("orange")
my.discard("mango") # or can use my.remove("mango")
print(my) 

li = ["hi",21,"Darshan"]
s = set(li)
t = tuple(li)
print(s)
print(t)
s.add(2123)
# In tuple we cant add 
print(s)

# Extra
n = int(input("Enter the value of n :"))
if n==1:
    print("The factorial of 1 is 1")
else:
    print(f"The factorial of {n} is : {n * factorial(n-1)}")
# we can't use factorial function over here
'''