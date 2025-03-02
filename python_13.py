# Lambda Functions , Recursion, key arguments and Kwargs(Key word argu)
'''
def add(a,b):
    return a+b
# print(add(1,2))

c = add(1,2)
print(c)

def d(*a):
    print(a) # Now a will be tuple
d(1,2,3,5,5,6)

def ad(*num):
    return sum(num)
print(ad(1,2,3,4,5))

def student_info(**details): # ** for key and values arguments
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")

# Lambda Function
add = lambda a,b: a+b
print(add(2,5))
double = lambda x,y,z: x*5
print(double(5,4,3))

student = [ # we can do this only in list but not in dic
    {"name":"Anand", "marks":89},
    {"name":"Darshan", "marks":99},
    {"name":"Apoo","marks":95}
]
student.sort(key=lambda x: x["marks"], reverse=True)
print(student)

# Recursion
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))
'''
# Nested Functions
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("Darshan")

def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)
    add()
    sub()
    mul()
    div()

calculate(5,5)

