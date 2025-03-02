# Loop Revision
'''
l = [21,23,43,54]
total = 0

for num in l:
    print(total)
    total = total + num
print("The total is :",total)

l = [21,45,654,65]
dl = []

for num in l:
    dl.append(num*2) # Doubleing the numbers
    print(dl)

marks = {"Darshan":98,"sneha":95,"apoo":90}

for students, mark in marks.items():
    print(f"{students}--{mark}")


students = ["Darshan","sneha","apoo"]
marks = [98,67,87]
dic = {}

for index, m in enumerate(students):
    dic[m]=marks[index]

print(dic)
# Another method if we know list size

for i in range(3): # for i in range(1,len(students)) covesr all
    dic[students[i]] = marks[i]
print(dic)
'''
# List Comprehension
'''
n= [1,2,3,4,5,6]
dn = [item+2 for item in n]
print(dn)

x = [x for x in range(1,11)]
d = [y**2 for y in x if y%2==0]
print(d)

# Dic
name = ["Darshan","Apoo","Ruthu"]
d = {n:len(n) for n in name}
print(d)

city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
la = {l:value for l,value in city_population.items() if value>10} 
print(la)
'''
# Splitting Strings to Create Lists
li = [1,2,3,4,5,6,7]
s = input("Enter the list no :").split()
l = [num for num in s]
print(l)
