"""
2 cases
case-1: How to access values outside the function
        - In this case, how to access name and company outside the function
case-2: How to pass values to variables present inside the function
        - In this case, how to pass values to name and company

Here,
case-1: How to access values outside the function
        - In this case, how to access name and company outside the function
"""

print("Function with 1 return value")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company)
    return name
    # From here only function execution will stop
    # and go back to where we are calling this function
    print("This will never print")
    # after the return statement if some statements are present then
    # it will never execute


received_value = employee()
print("received_value:", received_value)

print("#"*40)
###########################

print("Function with more than 1 return value: TUPLE")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company)
    return name, company # it will keep all values in tuple and return
    # From here only function execution will stop
    # and go back to where we are calling this function
    print("This will never print")
    # after the return statement if some statements are present then
    # it will never execute


received_value = employee()
print("received_value:", received_value)

print("#"*40)
###########################


print("Function with more than 1 return value: LIST")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company)
    return [name, company]
    # From here only function execution will stop
    # and go back to where we are calling this function
    print("This will never print")
    # after the return statement if some statements are present then
    # it will never execute


received_value = employee()
print("received_value:", received_value)

print("#"*40)
###########################

print("Function with more than 1 return value: DICTIONARY")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}
    # From here only function execution will stop
    # and go back to where we are calling this function
    print("This will never print")
    # after the return statement if some statements are present then
    # it will never execute


received_value = employee()
print("received_value:", received_value)

print("#"*40)
###########################
print("Function with NO return value: None")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company)
    return
    # From here only function execution will stop
    # and go back to where we are calling this function
    print("This will never print")
    # after the return statement if some statements are present then
    # it will never execute


received_value = employee()
print("received_value:", received_value)

print("#"*40)
###########################


print("Function with NO return statement: None")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company)


received_value = employee()
print("received_value:", received_value)

print("#"*40)
###########################


print("Function with EXPRESSION in return")
print("-"*20)
# ------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Name:", name)
    print("Company:", company)
    return (10+20)/(1-2) # return the result


received_value = employee()
print("received_value:", received_value)

print("#"*40)
###########################