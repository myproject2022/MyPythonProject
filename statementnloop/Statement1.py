# simple example of statement in python
import math

print("Enter user information")
last_name = input("enter your lastname ")
first_name = input("Enter your first name ")
age1 = input("Enter your age ")
gander = input("enter your gander ")
address = input("enter your address ")

full_name = first_name.capitalize() + "  " + last_name.capitalize()
# age = int(age1[,base6])
age = round(age1)

print("--------------------------------")
print("User detail Information\n\n")

if age < 21:
    print("This user is under the age to serve alcohol")
    print("Full Name :", full_name)
    print("Age :", age)
    print("Gander :", gander)
    print("Address :", address)

elif 21 < age < 65:
    print("This user is under the age to serve alcohol")
    print("Full Name :", full_name)
    print("Age :", age)
    print("Gander :", gander)
    print("Address :", address)

else:
    print("This user is under the age to serve alcohol")
    print("Full Name :", full_name)
    print("Age :", age)
    print("Gander :", gander)
    print("Address :", address)

# print("Full Name", full_name.upper())
