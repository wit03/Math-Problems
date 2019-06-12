Uinput = int(input("Enter Term: "));

up = 0
down = 0
sum = 0
oldSum = 0

for x in range(1, Uinput+1):
    up = x 
    down = x + 1
    print(" ")
    print("Round: ")
    print(x)
    if (up % 2 != 0):
        oldSum = sum
        sum = oldSum + up / down
        print(sum) 
    else :
        oldSum = sum
        sum = oldSum - up / down 
        print(sum)
    if (x == Uinput):
        print(" ")
        print("Sum of term: ")
        print(sum)
    


    