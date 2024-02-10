"""
- List of builtins

"""

print("Complete list of builtins")
print("-"*20)
# ------------

print(dir(__builtins__))

print("#"*40)
###########################

print("Numbers Example")
print("How to store numbers and print")
print("-"*20)
# ------------

# No premitive data types in python
# everything is object types

a = 10
# Internally it will create object of predefined class 'int' and store the value

# OR we can also store/create-object using class name
b = int(20)

print(a, b)

print("#"*40)
###########################
print("String PART-1")
print("How to store and print")
print("-"*20)
# ------------

a = 'WEL COME' # we can use ' OR " OR ''' OR """ quotes
# Internally it will create object of predefined class 'str' and store the value

# OR we can also store/create-object using class name
b = str('WEL COME')
print(a, b)

print("#"*40, end="\n\n")
###########################

print("String PART-2")
print("Indexes: We can access each character using Indexes")
print("-"*20)
# ------------

a = 'WEL COME'
print("a:", a, end="\n\n")

print("1st character:", a[0])
print("1st character using negative index:", a[-8], end="\n\n")

print("Sub string:", a[1:6])
print("Skip charter:", a[1:6:2], end="\n\n")

print("#"*40)
###########################

print("String PART-3")
print("List of methods present inside the class")
print("-"*20)
# ------------

print(dir(a))

# OR we can use class name
print(dir(str))

print("#"*40)
###########################
# ------------
# Why 2 naming conventions
###########
# - few method names are starting with __ and ending with __
# - these are system defined names
# - It is mapped to some functions or it may be mapped to some operators
# Example:
##>>> s1="Python"
##>>> s2 = "Hello"
##>>> s1 + s2
##'PythonHello'
##>>> # Internally + calls __add__, that means it calls like
##>>> s1.__add__(s2)
##'PythonHello'
###########################

print("String PART-4")
print("startswith method")
print("-"*20)
# ------------

a = "WEL COME"
print("a:", a)

result = a.startswith("WEL") # True/Fals
print('result:', result)

print("#"*40)
###########################
print("Tuple PART-1")
print("store the values and print")
print("-"*20)
# ------------

my_tuple = (10, 12.5, "Python", (100, 200))
print("my_tuple:", my_tuple)
# Internally it will create object of predefined class 'tuple' and store the value

# OR we can also store/create-object using class name
my_tuple = tuple((10, 12.5, "Python", (100, 200)))
print("my_tuple:", my_tuple)

print("#"*40)
###########################

# Indexes are similar to strings

print("Tuple PART-2")
print("list all methods")
print("-"*20)
# ------------

my_tuple = (10, 12.5, "Python", (100, 200))
print(dir(my_tuple))

# OR we can use class name
print(dir(tuple))

print("#"*40)
###########################
print("frozenset PART-1")
print("store the values and print")
print("-"*20)
# ------------

my_frozenset = frozenset({10, 10, 10, "Python", "Python", "Java", "Java"})
# Internally it will create object of predefined class 'frozenset' and store the value
# insertion order does not maintain.
print("my_frozenset :", my_frozenset )

print("#"*40)
###########################

# - Indexes are NOT THERE?
# - If we want we can convert to list/tuple etc
#   t = tuple(my_frozenset)
# - We can also iterate using loops

print("frozenset PART-2")
print("list of methods")
print("-"*20)
# ------------

print(dir(my_frozenset))

# OR we can also pass class name
# print(dir(frozenset))


print("#"*40)
###########################
print("Bytes PART-1")
print("How to store and print")
print("-"*20)
# ------------

a = b'WEL COME'
# Internally it will create object of predefined class 'bytes' and store the value

# OR we can also store/create-object using class name
b = bytes(b'WEL COME')
print(a, b)

print("#"*40, end="\n\n")
###########################

print("Bytes PART-2")
print("Indexes: We can access each character using Indexes")
print("-"*20)
# ------------

a = b'WEL COME'
print("a:", a, end="\n\n")

print("1st character(ascii):", a[0])
print("1st character:", chr(a[0]))

print("Sub string:", a[1:6])
print("Skip charter:", a[1:6:2], end="\n\n")

print("#"*40)
###########################

print("Bytes PART-3")
print("List of methods present inside the class")
print("-"*20)
# ------------

print(dir(a))

# OR we can use class name
#print(dir(bytes))

print("#"*40)
###########################

#
#
print("Bytes PART-4")
print("startswith method")
print("-"*20)
# ------------

a = b"WEL COME"
print("a:", a)

result = a.startswith(b"WEL") # True/False
print('result:', result)

print("#"*40)
###########################
print("List PART-1")
print("store the values and print")
print("-"*20)
# ------------

my_list = [10, 12.5, "Python", (100, 200)]
print("my_list:", my_list)
# Internally it will create object of predefined class 'list' and store the value

# OR we can also store/create-object using class name
my_list = list((10, 12.5, "Python", (100, 200)))
print("my_list:", my_list)

print("#"*40)
###########################

# Indexes are similar to strings

print("List PART-2")
print("list all methods")
print("-"*20)
# ------------

my_list = [10, 12.5, "Python", (100, 200)]
print(dir(my_list))

# OR we can use class name
# print(dir(list))

print("#"*40)
###########################
print("set PART-1")
print("store the values and print")
print("-"*20)
# ------------

my_set_1 = {10, 10, 10, "Python", "Python", "Java", "Java"}
# Internally it will create object of predefined class 'set' and store the value

my_set_2 = set({10, 10, 10, "Python", "Python", "Java", "Java"})

print(my_set_1, my_set_2)

print("#"*40)
###########################

# - Indexes are NOT THERE?
# - If we want we can convert to list/tuple etc
#   t = tuple(my_set_1)
# - We can also iterate using loops

print("set PART-2")
print("list of methods")
print("-"*20)
# ------------

print(dir(my_set_1))

# OR we can also pass class name
# print(dir(set))


print("#"*40)
###########################
print("Bytearray PART-1")
print("How to store and print")
print("-"*20)
# ------------

a = bytearray(b'WEL COME')
# Internally it will create object of predefined class 'bytearray' and store the value

# OR we can also store/create-object using class name
b = bytearray(b'WEL COME')
print(a, b)

print("#"*40, end="\n\n")
###########################

print("bytearray PART-2")
print("Indexes: We can access each character using Indexes")
print("-"*20)
# ------------

a = bytearray(b'WEL COME')
print("a:", a, end="\n\n")

print("1st character(ascii):", a[0])
print("1st character:", chr(a[0]))

print("Sub string:", a[1:6])
print("Skip charter:", a[1:6:2], end="\n\n")

print("#"*40)
###########################

print("bytearray PART-3")
print("List of methods present inside the class")
print("-"*20)
# ------------

print(dir(a))

# OR we can use class name
#print(dir(str))

print("#"*40)
###########################

print("bytearray PART-4")
print("startswith method")
print("-"*20)
# ------------

a = bytearray(b"WEL COME")
print("a:", a)

result = a.startswith(b"WEL") # True/Fals
print('result:', result)

print("#"*40)
###########################

s = "Anuaragaa"
print(s.find("g"))