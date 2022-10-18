"""
Here is sample simple example of decorator
"""

class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance +=1

    @staticmethod
    def printNumInstance():
        print("Number of Instance Created: ", Spam.numInstance)


a = Spam()
b = Spam()
b = Spam()
Spam.printNumInstance()
a.printNumInstance()