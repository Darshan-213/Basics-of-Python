# Loop functions (while Loop)

'''condition = True
while condition: # Continuese Loop
   print("Condition is True")

hello = True
i = 1
while hello:
    if i%2!=0: # is not even
        i = i+1
        continue
    print(i)  # Printing even numbers
    i = i + 1
    if i>30:
        break
    
i = 10
while i<=10:
    print(i*"*")
    i -= 1
    if i == 0:
       break

# attempts is called as iteration
i = 0
while i<=10:
    x=0
    while x<i:
        print("Darshan", end = "-") # print("Darshan",end="-") This will not
        #print darshan in next line
        x += 1
    print("")
    i += 1
'''
pin = 1234
trials = 0
#input_pin = int(input("Enter the Pin >>"))
while  trials<=3:
    input_pin = int(input(f"Trail no {trials} Enter the Pin >> :"))
    trials += 1
    if input_pin == pin:
        print("Correct Pin")
        break
    else:
        print("Worng Pin")

