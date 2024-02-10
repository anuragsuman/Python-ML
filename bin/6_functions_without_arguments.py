"""
Functions: If we want to rewrite/copy-paste same code more than
one time then instead of rewrite/copy-paste, keep that code
in a block and we can execute as many times as we want
"""

print("Without Using Function")
print("-"*20)
# ------------

a = 10
b = 20
result = a + b
print("result:", result)

a = 10
b = 20
result = a + b
print("result:", result)

a = 10
b = 20
result = a + b
print("result:", result)

a = 10
b = 20
result = a + b
print("result:", result)

print("#"*40)
###########################

print("Using Function")
print("-"*20)
# ------------

# Function Definition
# 'my_func' is function object
def my_func():
    a = 10
    b = 20
    result = a + b
    print("result:", result)


# Function call
my_func()
my_func()
my_func()
my_func()

print("#"*40)
###########################
print("Just another function, Nothing special here")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company, end="\n\n")


employee()
employee()
employee()

print("#"*40)
###########################

###########################
# Python Coding Standard OR Style Guide
###########################
# https://peps.python.org/pep-0008/
###########################