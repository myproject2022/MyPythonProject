# sample simple variable of python programming
class Student:
    tuition_fee = 25000
    def __init__(self):
        self.fname = input("Enter Student First Name: ")
        self.lname = input("Enter student Last Name: ")
        self.sid = int(input("Enter Student ID: "))
        self.tfee = float(input("Enter Student Tuition Fee: "))
        self.semail = self.lname + '.' + self.fname + '@school.edu'

    def sfee_raise(self):
        if Student.tuition_fee > 25000:
            self.fee = self.tfee + self.tfee * 0.03
        else:
            self.fee = self.tfee * 1.01

    def student_details(self):
        self.fullname = self.fname + " " +self.lname
        print(self.fullname)

std_obj1 = Student()
# std_obj1.sfee_raise()
print(std_obj1.sfee_raise())
std_obj1.student_details()