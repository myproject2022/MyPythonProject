# simple and sample example of oop class concept in python
class Employee:
    def __init__(self):
        self.fname = input("Enter Your first Name: ")
        self.lname = input("Enter Your last name: ")
        self.salary = input("Enter Your annual salary: ")

        print("First Name :", self.fname)
        print("Last Name :", self.lname)
        print("Salary per year :", self.salary)
        print("Email :", self.lname + '.' + self.fname + '@gmail.com')
Employee()
# print(emp_obj1)