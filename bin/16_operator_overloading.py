"""
Operator Overloading:

if we use + b/n 2 int class object then it will add 2 nos
if we use + b/n 2 str class object then it will concatinate 2 strings

Similarly,
we can also support for any operators in our class

In python for each operator there is SPECIAL NAME given
example: for '+' SPECIAL NAME IS __add__
example: for '-' SPECIAL NAME IS __sub__

If we want to support any of the operator then
we need write a method using SPECIAL NAME for that operator
"""

# print("Operator Overloading Example-1")
# print("-"*20)
# # ------------
#
# class Employee:
#     def __init__(self, en):
#         self.name = en
#
#
# e1 = Employee("emp-1")
# e2 = Employee("emp-2")
# result = e1 + e2
# print("result:", result)
#
# # Since Operator + is not supported,
# # BELOW ERROR WE WILL GET
# # ------------
# # Traceback (most recent call last):
# #   File "C:\python_training\bin\16_operator_overloading.py", line 29, in <module>
# #     result = e1 + e2
# #              ~~~^~~~
# # TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
# # ------------
#
# print("#"*40, end="\n\n")
# ###########################


print("Operator Overloading Example-2")
print("-"*20)
# ------------

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self=e1, other=e2
        result = self.name + other.name
        return result



e1 = Employee("emp-1")
e2 = Employee("emp-2")
# REQUIREMENT: It should concatinate both employee names
result = e1 + e2 # e1.__add__(e2)
print("result:", result)


print("#"*40, end="\n\n")
###########################