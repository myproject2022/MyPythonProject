# Sample of oop class concept in python
class Employees:
    def __init__(self, fname, lname, dept, role, pay):
        self.fname = fname
        self.lname = lname
        self.dept = dept
        self.role = role
        self.pay = pay
        self.email = lname + '.' + fname + '@company.com'

    def full_name(self):
        return '{}'.format(self.fname + " " + self.lname)

emp_obj = Employees('Sanoj', 'Panta', 'dev', 'Engineer', 180000)
print(emp_obj.email)
# print(emp_obj.full_name())
print(Employees.full_name(emp_obj))