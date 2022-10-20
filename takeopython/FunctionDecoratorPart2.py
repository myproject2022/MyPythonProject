"""
Simple Code for
"""
#
#
# class FunctionDecorator1:
#
#
# obj1 = FunctionDecorator1
# obj1.printFunct("si")


def printFunct(stnc):
    def prinString():
        print("This is first String First")
        stnc()
        print("Second String:")
        return stnc

    return prinString()


@printFunct
def secondPrinting():
    print("Here is Second Print")


s = secondPrinting
x = printFunct(s)
x()
