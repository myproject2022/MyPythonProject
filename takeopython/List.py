print("some example of the list")

exl = [1, 1, 3, 5, 7, 9, 13, 27, 23, 29, 31]
print("print list" + "---->" + str(exl))

print("remove last index from the list" + "----->" + str(exl.remove(31)) + str(exl))
print(exl)

# use of append in list
exl.append(37)
# print(d)
print(exl)

# use of delete
del(exl[10])
print(exl)

# remove method for the list
exl.append(47)
print(exl)

exl.sort()
print(exl)

# print the double line of list

print(exl * 2)