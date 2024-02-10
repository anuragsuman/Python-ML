"""
Inheritance
- multilevel inheritance
- multiple inheritance
"""
print("Multilevel Inheritance")
print("-"*20)
# ------------


# Assume This is Existing class
class Salary:
    def add_salary(self, s):
        self.salary = s
    def get_salary(self):
        return self.salary

# New Requirement:
# Extend existing class to add below features
# 1) add tax
# 2) get tax
# 3) modify get_salary() to return (salary-tax)

class Employee(Salary):
    def add_tax(self, t):
        self.tax = t
    def get_tax(self):
        return self.tax
    # 3) modify get_salary() to return (salary-tax)
    # POLYMORPHISM: We can use same name as super class method
    def get_salary(self):
        # return self.salary - self.tax
        #
        # HERE we are calling super class get_salary
        super_salary = super().get_salary()
        return super_salary - self.tax


e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.get_salary())
print("tax:", e1.get_tax())

print("#"*40, end="\n\n")
###########################
print("Multiple Inheritance")
print("-"*20)
# ------------


class Salary:
    def add_salary(self, s):
        self.salary = s
    def get_salary(self):
        return self.salary


class Tax:
    def add_tax(self, t):
        self.tax = t
    def get_tax(self):
        return self.tax

# Requirement:
# Create class which is having below functionality
# 1) add/view salary
# 2) add/view tax
# 3) add/view employee name

class Employee(Salary, Tax):
    def add_employee_name(self, en):
        self.name = en
    def get_employee_name(self):
        return self.name


e1 = Employee()
e1.add_salary(2000)
e1.add_tax(200)
e1.add_employee_name("emp-1")

print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())
print("Name", e1.get_employee_name())

# 1st look for current class for the method
# then look for super class LEFT to RIGHT
#   which means, check in 'Salary' 1st then goto 'Tax' class

print("#"*40, end="\n\n")
###########################
print("Composite Object: One object HAS-A other object")
print("-"*20)
# ------------


class NewTax:
    def add_tax(self, t):
        self.tax = t
    def get_tax(self):
        return self.tax

class OldTax:
    def add_tax(self, t):
        self.tax = t + 100
    def get_tax(self):
        return self.tax + 100

# ---------
# Always NewTax Methods will execute in this class
# ---------
# class Employee(NewTax, OldTax):
#     def add_employee_name(self, en):
#         self.name = en
#     def get_employee_name(self):
#         return self.name
# ---------

class Employee(NewTax):
    def __init__(self):
        self.oldtax_obj = OldTax()
    def add_employee_name(self, en):
        self.name = en
    def get_employee_name(self):
        return self.name


e1 = Employee()
e1.add_employee_name("emp-1")
e1.add_tax(2000)
e1.oldtax_obj.add_tax(200)

print("Name:", e1.get_employee_name())
print("NewTax:", e1.get_tax())
print("OldTax:", e1.oldtax_obj.get_tax())

print("#"*40, end="\n\n")
###########################
###########################