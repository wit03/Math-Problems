max = int(input("Enter Max: "))
userType = str(input("Enter odd or even: "))
sum = 0
oldX = 0

for x in range(1, max+1):
        if userType == "odd":
                if x % 2 != 0:
                        oldX = sum
                        sum = x + oldX
        else:
                if x % 2 == 0:
                        oldX = sum
                        sum = x + oldX

print(sum)