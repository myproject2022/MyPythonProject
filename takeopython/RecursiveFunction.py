"""
Here is some example of recursive function
"""


def mynumb(l):
    print(l)
    if not l:
        return 0
    else:
        return l[0] + mynumb(l[1:])


mynumb([1, 2, 3, 4, 5])
# print(mynumb())
