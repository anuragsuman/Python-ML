"""
How to store the data and get the data?

3-way to store the data and get the data

In this section, we should get 100% clarity on
1. __new__ : Constructor
2. __init__ : Initializer
"""

print("Constructor and Initializer")
print("-"*20)
# ------------


class Employee:
    company_name = "XYZ Company"
    # if we write some variables inside the class
    # then it will get stored inside CLASS OBJECT only

    def __init__(self, en):
        self.name = en

    @classmethod
    def get_company_name(cls):
        return cls.company_name


    def get_employee_name(self):
        return self.name

    @staticmethod
    def compute_avg_salary(sal1, sal2):
        return (sal1 + sal2)/2
    # No object will be passed in 1st argument


e1 = Employee("emp-1")
# It will create brandnew object and store in e1
e2 = Employee("emp-2")
# It will create brandnew object and store in e2

s1 = 2000
s2 = 3000
avg_salary = Employee.compute_avg_salary(s1, s2)

print("Company_name:", Employee.get_company_name()) # get_company_name(Employee), cls=Employee
print("e1 Name:", e1.get_employee_name())  # get_employee_name(e1) # self=e1
print("e2 Name:", e2.get_employee_name())  # get_employee_name(e2) # self=e2
print("avg_salary:", avg_salary)

print("#"*40, end="\n\n")
###########################

# ------------
# About 'object' class
# ------------
# - it is builtin
# - it has many methods
# - 2 of them are
#   1) __new__()
#   2) __init__()
# - inside __new__() method we have logic
#   to CONSTRUCT THE OBJECT
# - __init__() method is EMPTY
###########################

# ------------
# About 'Employee' class
# ------------
# - Internally all classes which we write
#   by default linked to 'object'
#   this linking is also called 'INHERITANCE'
# - 'object' class also called PARENT/SUPER class
#   'Employee', we can call CHILD/SUB
# - Whatever present inside object class
#   can be accessed from our class 'Employee'
#
# - When we create object of 'Employee' class
#   Internally it will call 2 methods
#   1) __new__() to construct the object
#   then
#   automatically __init__() method will be called
# - We can always rewrite same methods present in super class
#   using same name (POLYMORPHISM)
#   and
#   if we call those methods which is present in both
#   then 1st it will check in current class, if not present
#   then only it will execute super class method
# - In above class since we have __init__ in our class
#   __new__ will be executed from super class and __init__
#   executed from our class
#
# - We can always execute current class method and also super class methods
#   which is having same name
###########################