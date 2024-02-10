"""
2-way: we can pass values to name and company in key=value format

How to pass values to name and company using 2nd way?

Functions with KEYWORD or NAMED arguments
"""

print("Function with KEYWORD or NAMED ARGUMENTS")
print("-"*20)
# ------------


# name, company are called KEYWORD or NAMED ARGUMENTS
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee(name="emp-1", company="xyz company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

received_value = employee(company="xyz company", name="emp-2") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-3", company="ABC company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

print("#"*40)
###########################
print("Function with DEFAULT VALUE KEYWORD or NAMED ARGUMENTS")
print("-"*20)
# ------------


# name, company are called KEYWORD or NAMED ARGUMENTS
def employee(*, name, company="XYZ COMPANY"):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee(name="emp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-2", company="xyz company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-3", company="ABC company") # pass in same order as definition
print("received_value:", received_value, end="\n\n")

# ORDER OF THE ARGUMENT IN FUNCTION DEFINITION
# 1st put all non-default value POSITIONAL arguments IF ANY
# then
# 1st put all default value POSITIONAL arguments IF ANY
# then
# put variable POSITIONAL arguments IF ANY
# then
# put all default/non-default KEYWORD or NAMED arguments in any order

print("#"*40)
###########################
print("Function with VARIABLE KEYWORD or NAMED ARGUMENTS")
print("-"*20)
# ------------


# name, company are called KEYWORD or NAMED ARGUMENTS
# *prev_companies called VARIABLE KEYWORD or NAMED ARGUMENTS
def employee(*, name, company="XYZ COMPANY", **prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("pre_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee(name="emp-1")
# name ='emp-1', company="XYZ COMPANY", prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-2", company="xyz company")
# name ='emp-2', company="xyz company", prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-3", company="ABC company")
# name ='emp-3', company="ABC company", prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-4", company="ABC company", pc1="prev_comp_1")
# name ='emp-4', company="ABC company", prev_companies = {pc1: "prev_comp_1"}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-5", company="ABC company", pc1="prev_comp_1", pc2="prev_comp_2")
# name ='emp-5', company="ABC company", prev_companies = {pc1:"prev_comp_1", pc2: "prev_comp_2"}
print("received_value:", received_value, end="\n\n")

# ORDER OF THE ARGUMENT IN FUNCTION DEFINITION
# 1st put all non-default value POSITIONAL arguments IF ANY
# then
# 1st put all default value POSITIONAL arguments IF ANY
# then
# put variable POSITIONAL arguments IF ANY
# then
# put all default/non-default KEYWORD or NAMED arguments in any order IF ANY
# then
# put variable KEYWORD arguments IF ANY


print("#"*40)
###########################
# ------------
# Possible argument combinations
# ------------
# 1
# def add(a,b)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 2
# def add(a,b=10)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 3
# def add(b=10, a)
# NOTE: Check the order -> WRONG ORDER OF THE ARGUMENT
#
# 4
# def add(a,b=10, *c)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 5
# def add(*,a,b)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 6
# def add(*,a=10,b)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 7
# def add(*,a,b=10)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 8
# def add(a, b, *, c, d)
# NOTE: Check the order -> CORRECT FUNCTION
# How to call? add(10,20,c=30,d=40)
#
# 9
# def add(*a)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 10
# def add(**a)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 11
# def add(*a, **b)
# NOTE: Check the order -> CORRECT FUNCTION
#
# 12
# def add(**a, *b)
# NOTE: Check the order -> WRONG ORDER
#
#
# 13: ALL IN ONE
# def add(a, b=10, *c, d, e=20, **f)
# NOTE: Check the order -> CORRECT FUNCTION
#
###########################

print("All In One")
print("-"*20)
# ------------


def add(a, b=10, *c, d, e=20, **f):
    return a + b + sum(c) + d + e + sum(f.values())


add_result_1 = add(10, d=20)
# a = 10, b = 10, c = (), d=20, e=20, f={}
print("add_result_1:", add_result_1)

add_result_2 = add(10, 20, 30, 40, 50, d=60, e=70, x=80, y=90, z=100)
# a = 10, b = 20, c = ( 30, 40, 50), d=60, e=70, f={x=80, y=90, z=100}
print("add_result_2:", add_result_2)

print("#"*40)
###########################


# def print(*values: object,
#           sep: str | None = ...,
#           end: str | None = ...,
#           file: SupportsWrite[str] | None = ...,
#           flush: bool = ...) -> None
#
# -------
# 1st Call: print function
# -------
# print(10, 20, 30, 40)
# values = (10, 20, 30, 40)
# sep=' '
# end='\n'
# file=STDOUT
# flush=None
#####################

# -------
# 1st Call: print function
# -------
# print(10, 20, 30, 40, sep='|', end='\n\n')
# values = (10, 20, 30, 40)
# sep='|'
# end='\n\n'
# file=STDOUT
# flush=None
#####################