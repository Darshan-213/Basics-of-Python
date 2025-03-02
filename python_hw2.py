# Dictionaries in Python
'''
dic = {
    "Bangalore":"palav",
    "hassan":"dosa",
    "mangalure":"fish",
    "mysore":"idali",
    "madugiri":"vada"
}
dic["shivamoga"] = "kadubu"
dic["Bangalore"] = "Biryani"
del dic["hassan"]
print(dic.keys())
print(dic.values())
print(dic)

dic = {
    "fri1":{
        "name":"darshan",
        "sub":"maths",
        "food":"Biryani"
    },
    "fri2":{
        "name":"apoo",
        "sub":"accounts",
        "food":"idali"
    }
}
print(dic["fri1"]["food"])

age = int(input("Enter Your age : "))
if age<=5:
    print("Bus pass is Free")
elif age>=60:
    print("You get senior citizen discount")
else:
    print("Pay full amount for Bus pass")

time = input("Enter the time : ")
if time == "8 am":
    print("It's Breakfast time")
elif time=="1 pm":
    print("It's lunch time")
elif time == "8 pm":
    print("It's Dinner time")
else:
    print("It's not meal time")

i = 1
while i<=20:
    if i%2!=0:
        print(i)
    i += 1

seat = 8
while seat>0:
    print("Book 1 seat")
    seat -= 1
    print("Remaining seats",seat)
print("All seats are booked")

i = 10
while i<=10:
    print(i)
    i -= 1
    if i == -1:
        print("Happy New Year")
        break

for i in range(1,11):
    print(f"3x{i}={3*i}")

sum = 0
for i in range(1,11):
    sum = sum + i # print(10*11/2) , n*n+1/2 for n numbers
    
print(sum)

name = input("Enter the name : ")
for letter in name:
    print(letter)

vowels = "aeiou"
sen = input("Enter the string : ")
count = 0
for letter in sen:
    if letter in vowels:
        count += 1
        print(letter)
print(count)
'''


