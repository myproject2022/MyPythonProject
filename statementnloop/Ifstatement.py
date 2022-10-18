# simple example of if statement in python
a = 12
b = 24
list = [1, 2, 3, 4, 5]

if a in list:
    print("a in a list")
else:
    print("a not in the list")
if b not in list:
    print("true")
else:
    print("false")

c = b/a
if c in list:
    print("true value", c)
else:
    print("false value", c)