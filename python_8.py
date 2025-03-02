# if, esle, elif, while and for 
''' # if , elif and else
age = int(input("Enter your age :"))
if age >= 18:
    print("You can Drive")
    print("You can Vote")
elif age >= 10:
    print("You can ride Bicycle")
    print("You can't Vote")
else:
    print("You can't Drive and ride Bycycle")
'''
# Nested If
day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")
