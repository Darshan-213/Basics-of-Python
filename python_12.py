# Functions 
def greet():
    print("Hello Good Night")
    
greet()

# Tables
def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
#table(7)

# marriage 
def marriage(boy,girl="Girl"): # defult value girl = "Girl" if girl is not given
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} loves {girl}")

#marriage("Darshan")

# Return Function
def func(num):
    return(str(num)*2)
a = int(func(2))
c = a+12
print(c)

# Local Variable
def fun():
    x = "Darshan" # local variable
    print("Hello world")
    print(y) # we can access here also because it is global

y = "Apoo" # global variable
#print(x) # we can't access x because it is local variable
print(y) # we can because it's global variable

