min = int(input("Enter min: "))
max = int(input("Enter max:"))
sum = 0
oldX = 0
for x in range(min, max+1):
    if x % 2 == 0:
        sum = x + oldX
        oldX = sum
        print(sum)
            