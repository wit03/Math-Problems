userInput = int(input("Enter !: "))
sum = 1
oldSum = 1

for x in range(1, userInput+1):
    oldSum = sum
    sum = x * oldSum;
    if (x == userInput):
        print("Sum: ")
        print(sum)