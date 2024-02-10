"""
How to store the data and get the data?

1-way to store the data and get the data

In this section, we should get 100% clarity on
1. CLASS VARIABLES
2. INSTANCE VARIABLES
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

print("Store the Data and Get the Data")
print("-"*20)
# ------------

# ------------
# 1-way to Store
# ------------
Employee.company_name = "XYZ Company"
# It will create new variable 'company_name' inside 'Employee' object and store the value
e1.name = 'emp-1'
# It will create new variable 'name' inside 'e1' object and store the value
e2.name = 'emp-2'
# It will create new variable 'name' inside 'e2' object and store the value
# ------------

# ------------
# Print the values
# ------------
print("Company_name:", Employee.company_name, sep="\n", end="\n\n")
print("'e1 Name':", e1.name, sep="\n", end="\n\n")
print("'e2 Name':", e2.name, sep="\n", end="\n\n")
# ------------

print("#"*40, end="\n\n")
###########################

print("Inside CLASS OBJECT and INSTANCE OBJECTS")
print("-"*20)
# ------------

print("Inside CLASS OBJECT 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("Inside INSTANCE OBJECT 'e1':", dir(e1), sep="\n", end="\n\n")
print("Inside INSTANCE OBJECT 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################
print("We can access data present inside 'CLASS OBJECT' using 'INSTANCE OBJECTS'")
print("-"*20)
# ------------

print("Access Company_name using CLASS OBJECT 'Employee':", Employee.company_name, sep="\n", end="\n\n")
print("Access Company_name using INSTANCE OBJECT 'e1':", e1.company_name, sep="\n", end="\n\n")
print("Access Company_name using INSTANCE OBJECT 'e2':", e2.company_name, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

# ------------
# Why CLASS OBJECT?
# ------------
# - CLASS OBJECT is common space for all INSTANCE OBJECTS
# - Data which is common for all instances that can
#   be stored inside CLASS OBJECT
#
#   - if CLASSOBJECT is not present then we may need to store same data
#   in all instance objects which is waste of memory
#   - Since we have class object, we can keep common data there
###########################