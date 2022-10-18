"""
an example of class and object
"""


class Persion:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


# if __name__ == '__main__' :
# obj1 = Persion('san dai', 1000, )
# print(obj1.name, obj1.job, obj1.pay)
# print(obj1.name.split()[1])
# # print(obj1.name.capitalize())
# # print(obj1.name.appends([]))
# obj1.pay *= 1.05
# print(obj1.pay)