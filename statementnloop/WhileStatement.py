# simple sample example of the while loop
num = int(input("Enter number"))

while num < 20:
    print(num)
    num = num + 1

print("--------------------------------------------")
if num == 20:
    print("Number is equal to 20")
elif num != 20:
    print("Not equal to 20")
    while num != 0:
        print(num)
        num = num - 1

print("-----------")
while 10 > num > 5:
    print(num)
    num = num + 1
