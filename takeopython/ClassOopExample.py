"""
oop class example
"""
from takeopython.Class_N_ObjectExample import Persion


class Child(Persion):
    def setLastName(self):
        return self.name.split()[-1]

    def giveBonus(self, bonus):
        self.pay = int(self.pay + bonus)


obj2 = Child('san dai', 'dev', 5000)
print(obj2.name)
print(obj2.setLastName())
# print(obj2.giveBonus(1000))
obj2.giveBonus(1000)
print(obj2.pay)