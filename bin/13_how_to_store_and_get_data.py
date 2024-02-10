"""
How to store the data and get the data?

2-way to store the data and get the data

In this section, we should get 100% clarity on
1. CLASS METHODS
2. INSTANCE METHODS
"""

print("Class with methods")
print("-"*20)
# ------------


class Employee:
    @classmethod
    def store_company_name(cls, cn):
        cls.company_name = cn

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def store_employee_name(self, en):
        self.name = en

    def get_employee_name(self):
        return self.name

    @staticmethod
    def compute_avg_salary(sal1, sal2):
        return (sal1 + sal2)/2
    # No object will be passed in 1st argument


e1 = Employee()
# It will create brandnew object and store in e1
e2 = Employee()
# It will create brandnew object and store in e2

# Total 3 objects
# CLASS OBJECT: 'Employee' which is automatically getting created
# INSTANCE OBJECTS: 'e1' and 'e2' which we created

# ------------
# Store the data inside CLASS OBJECT 'Employee'
# ------------
Employee.store_company_name("XYZ Company")
#
#     def store_company_name(cls, cn):
#         cls.company_name = cn
#
# Internally
#
#     def store_company_name(Employee, "XYZ Company"):
#         Employee.company_name = "XYZ Company"
#
# 'cls': is to hold CLASS OBJECT reference
#
# about @classmethod:
#   - this is function only and called DECORATOR
#   - Inside this decorator we have some extra functionality
#       that is getting added our function
#
# Few POINTS
# - We can access class methods/varaibles using INSTANCE OBJECTS as well
# - Now if we access like,
#   e1.store_company_name("XYZ Company")
#   by default 'e1' will be passed to 'cls'
#   BUT
#   BUT
#   BUT
#   for this method, 100% we need to pass CLASS OBJECT only
#   instead of INSTANCE OBJECT eventhough we are calling using e1, e2 etc
# - @classmethod decorator will make sure to pass CLASS OBJECT only
#   eventhough we are calling using e1, e2 etc
#
#   So, if we are calling like
#   e1.store_company_name("XYZ Company")
#   internally
#   store_company_name(Employee, "XYZ Company") # 'Employee' will be passed, NOT e1
# ------------

# ------------
# Store data inside 'e1'
# ------------
e1.store_employee_name("emp-1")
#
#     def store_employee_name(self, en):
#         self.name = en
#
# Internally
#
#     def store_employee_name(e1, en):
#         e1.name = en
#
# 'self': 'self' is to hold instance object reference
# ------------

# ------------
# Store data inside 'e2'
# ------------
e2.store_employee_name("emp-2")
#
#     def store_employee_name(self, en):
#         self.name = en
#
# Internally
#
#     def store_employee_name(e2, en):
#         e2.name = en
#
# 'self': 'self' is to hold instance object reference
# ------------

s1 = 2000
s2 = 3000
avg_salary = Employee.compute_avg_salary(s1, s2)

print("Company_name:", Employee.get_company_name()) # get_company_name(Employee), cls=Employee
print("e1 Name:", e1.get_employee_name())  # get_employee_name(e1) # self=e1
print("e2 Name:", e2.get_employee_name())  # get_employee_name(e2) # self=e2
print("avg_salary:", avg_salary)

print("#"*40, end="\n\n")
###########################