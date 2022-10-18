from takeopython.ClassInherit import Shape


class Circle(Shape):
    def areaOfCircleGetValue(self, r):
        # self.area = self.radios * self.radios * pi
        # print("Area: ", self.area)
        self.radios = r
        print(r)

    def setValue(self, pi=3.13):
        self.area = pi * self.radios * self.radios
        print(self.area)

circle_obj = Circle(3, 3, 3, 3)
print(circle_obj.areaOfCircleGetValue(2))
# circle_obj.areaOfCircleGetValue(3)
print(circle_obj.setValue())
