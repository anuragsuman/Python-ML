"""
How to obtain or create objects?
- Answer: Using classes we can create objects

In this section, we should get 100% clarity on
1. CLASS OBJECT
2. INSTANCE OBJECTS
"""

print("CLASS OBJECT and INSTANCE OBJECTS")
print("-"*20)
# ------------


class Employee:
    pass
    # - pass: to keep any block like if, for, function etc use 'pass' dummy keyword
    # - Above class is valid class eventhough it is EMPTY


e1 = Employee()
# It will create brandnew object and store in e1
e2 = Employee()
# It will create brandnew object and store in e2

# Total 3 objects
# CLASS OBJECT: 'Employee' which is automatically getting created
# INSTANCE OBJECTS: 'e1' and 'e2' which we created

print("BrandNew CLASS OBJECT 'Employee':", Employee, sep="\n", end="\n\n")
print("BrandNew INSTANCE OBJECT 'e1':", e1, sep="\n", end="\n\n")
print("BrandNew INSTANCE OBJECT 'e2':", e2, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Inside CLASS OBJECT and INSTANCE OBJECTS")
print("-"*20)
# ------------

print("Inside BrandNew CLASS OBJECT 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("Inside BrandNew INSTANCE OBJECT 'e1':", dir(e1), sep="\n", end="\n\n")
print("Inside BrandNew INSTANCE OBJECT 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################