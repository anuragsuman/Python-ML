"""
case-2: How to pass values to variables present inside the function
        - In this case, how to pass values to name and company

2 ways to pass values to name and company
1-way: we can pass DIRECT values to name and company
2-way: we can pass values to name and company in key=value format

Here
1-way: we can pass DIRECT values to name and company
- Also called FUNCTIONS WITH POSITIONAL ARGUMENTS
"""

print("Function with POSITIONAL ARGUMENTS")
print("-"*20)
# ------------


# name, company are called POSITIONAL ARGUMENTS
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee("emp-1", "xyz company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "xyz company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-3", "ABC company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

print("#"*40)
###########################
print("Function with DEFAULT VALUE POSITIONAL ARGUMENTS")
print("-"*20)
# ------------


# name, company are called POSITIONAL ARGUMENTS
def employee(name, company="XYZ COMPANY"):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee("emp-1") # company will make use of default value
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "xyz company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-3", "ABC company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

# ORDER OF THE ARGUMENT IN FUNCTION DEFINITION
# 1st put all non-default value arguments
# then
# put all default value arguments

print("#"*40)
###########################
print("Function with VARIABLE POSITIONAL ARGUMENTS")
print("-"*20)
# ------------


# name, company are called POSITIONAL ARGUMENTS
# *prev_companies called VARIABLE POSITIONAL ARGUMENTS
def employee(name, company="XYZ COMPANY", *prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("pre_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee("emp-1")
# name ='emp-1', company="XYZ COMPANY", prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "xyz company")
# name ='emp-2', company="xyz company", prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-3", "ABC company")
# name ='emp-3', company="ABC company", prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-4", "ABC company", "prev_comp_1")
# name ='emp-4', company="ABC company", prev_companies = ("prev_comp_1")
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-5", "ABC company", "prev_comp_1", "prev_comp_2")
# name ='emp-5', company="ABC company", prev_companies = ("prev_comp_1", "prev_comp_2")
print("received_value:", received_value, end="\n\n")

# ORDER OF THE ARGUMENT IN FUNCTION DEFINITION
# ---------
# 1st put all non-default value arguments
# then
# put all default value arguments
# then
# put variable positional arguments

print("#"*40)
###########################
print("Maximum 1 varaible positional argument we can write")
print("If we need more than 1 then we can customize")
print("-"*20)
# ------------

def my_test_func(name, company, languages, skills, *prev_companies):
    print("Values inside the function:")
    print(name, company, languages, skills, prev_companies, sep="\n", end="\n\n")

l = ['l1', 'l2']
s = {'s1':'skill1', 's2': 'skill2'}
my_test_func('emp-1', 'xyz company', l, s, 'prev_comp_1', 'prev_comp_2')

# ORDER OF THE ARGUMENT IN FUNCTION DEFINITION
# ---------
# 1st put all non-default value arguments IF ANY
# then
# put all default value arguments IF ANY
# then
# put variable positional arguments IF ANY

print("#"*40)
###########################